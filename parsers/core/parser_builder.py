from abc import ABC, abstractmethod
from .category_parser import CategoryParser

class ParserBuilder(ABC):
    
    @abstractmethod
    def build(self) -> CategoryParser:
        pass
