from abc import ABC, abstractmethod
from .category_parser import CategoryParser
from saves import ISaveManager

class ParserBuilder(ABC):
    _save_manager: ISaveManager
    
    def __init__(self, save_manager: ISaveManager):
        self._save_manager = save_manager
    
    @abstractmethod
    def build(self) -> CategoryParser:
        pass
