# import abstract
from abc import ABC, abstractmethod,abstractclassmethod

class Country(ABC):
    def __init__(self,name,population) -> None:
        super().__init__()
        self.name = name
        self.pop = population

    def show_detail(self):
        pass