from abc import ABC, abstractmethod

class ISaveManager(ABC):
    @abstractmethod
    def add_to_buffer(self, objects: list[dict]):
        pass
    
    @abstractmethod
    def save_file(self):
        pass
    
