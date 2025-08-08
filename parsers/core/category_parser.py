from .parser import Parser
from .page_parser import PageParser
from abc import ABC, abstractmethod

class CategoryParser(Parser, ABC):
    _page_parser: PageParser
    
    def __init__(self, page_parser: PageParser):
        self._page_parser = page_parser
        
    def parse(self, url: str) -> list[dict]:
        self._set_url(url)
        
        result = []
        page_count = self._get_page_count()
        for page_number in range(1, page_count+1):
            page_url = self._get_page_url(url, page_number)
            result.extend(self._page_parser.parse(page_url, page_number))
            
        return result
        
    @abstractmethod
    def _get_page_url(self, url: str, page_number: int) -> str:
        pass
    
    @abstractmethod
    def _get_page_count(self) -> int:
        pass
