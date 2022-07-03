from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,barnd,speed) -> None:
        super().__init__()
        self.barnd = barnd
        self.speed = speed
        self.gear  = 0
        self.seat = 0

    def show_detail(Self):
        pass
    
