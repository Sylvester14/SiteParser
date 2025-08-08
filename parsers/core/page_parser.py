from .parser import Parser
from .product_parser import ProductParser
from abc import ABC, abstractmethod
from tqdm import tqdm

class PageParser(Parser, ABC):
    _product_parser: ProductParser
    
    def __init__(self, product_parser: ProductParser):
        self._product_parser = product_parser
    
    def parse(self, url: str, page_number: int) -> list[dict]:
        self._set_url(url)
        
        result = [] 
        for product_url in tqdm(self._get_products_url(), f"Обработка страницы {page_number}", leave=False):
            product_data = self._product_parser.parse(product_url) 
            result.append(product_data)
            
        return result
            
    
    @abstractmethod
    def _get_products_url(self) -> list[str]:
        pass
