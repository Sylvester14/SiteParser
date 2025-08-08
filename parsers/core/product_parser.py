from .parser import Parser
from abc import ABC, abstractmethod

class ProductParser(Parser, ABC):
    def parse(self, url: str) -> dict:
        self._set_url(url)
        
        image = self._parse_image()
        price = self._parse_price()
        name = self._parse_name()
        features = self._parse_features()
        
        return {
            "url": self._url,
            "url_image": image,
            "price": price,
            "name": name,
            "features": features
        }
        
    @abstractmethod
    def _parse_image(self) -> str:
        pass

    @abstractmethod
    def _parse_price(self) -> int:
        pass


    @abstractmethod
    def _parse_name(self) -> str:
        pass
    
    @abstractmethod
    def _parse_features(self) -> dict: 
        pass
