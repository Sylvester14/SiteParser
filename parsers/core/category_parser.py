from .parser import Parser
from .page_parser import PageParser
from saves import ISaveManager
from abc import ABC, abstractmethod
from tqdm import tqdm

class CategoryParser(Parser, ABC):
    _page_parser: PageParser
    _save_manager: ISaveManager
    
    def __init__(self, page_parser: PageParser, save_manager: ISaveManager):
        self._page_parser = page_parser
        self._save_manager = save_manager
        
    def parse(self, url: str):
        self._set_url(url)
        
        page_count = self._get_page_count()
        for page_number in tqdm(range(1, page_count+1), "Обработка категории"):
            page_url = self._get_page_url(url, page_number)
            page_data = self._page_parser.parse(page_url, page_number)
            
            self._save_manager.add_to_buffer(page_data)
        
    @abstractmethod
    def _get_page_url(self, url: str, page_number: int) -> str:
        pass
    
    @abstractmethod
    def _get_page_count(self) -> int:
        pass
