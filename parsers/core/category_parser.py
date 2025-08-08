from .parser import Parser
from .page_parser import PageParser
from saves import ISaveManager
from abc import ABC, abstractmethod
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

class CategoryParser(Parser, ABC):
    _page_parser: PageParser
    _save_manager: ISaveManager
    
    def __init__(self, page_parser: PageParser, save_manager: ISaveManager):
        self._page_parser = page_parser
        self._save_manager = save_manager
        
    def parse(self, url: str, max_page: int = -1, max_workers: int = 10):
        self._set_url(url)
        
        page_count = self._get_page_count()
        if(max_page != -1):
            page_count = min(page_count, max_page)
        
        # Обработка страниц в разных потоках
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.__parse_page, url, page_number) : page_number
                for page_number in range(1, page_count + 1)
            }
            
            for future in tqdm(as_completed(futures), total=len(futures), colour="green", desc="Обработка категории"):
                try:
                    future.result()
                except Exception as e:
                    raise Exception(f"Ошибка при обработки страницы: {e}")
            
    def __parse_page(self, url: str, page_number: int):
        page_url = self._get_page_url(url, page_number)
        page_data = self._page_parser.parse(page_url, page_number)
        
        self._save_manager.add_to_buffer(page_data)
        
    @abstractmethod
    def _get_page_url(self, url: str, page_number: int) -> str:
        pass
    
    @abstractmethod
    def _get_page_count(self) -> int:
        pass
