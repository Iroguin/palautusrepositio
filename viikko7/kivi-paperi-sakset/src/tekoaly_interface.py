from abc import ABC, abstractmethod

class TekoalyInterface(ABC):
    @abstractmethod
    def anna_siirto(self):
        pass
    
    @abstractmethod
    def aseta_siirto(self, siirto):
        pass