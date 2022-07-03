from vehicleapstract import Vehicle

class Car(Vehicle):
    def __init__(self, barnd, speed) -> None:
        super().__init__(barnd, speed)
        self._year = 0
        self._maintanance = 0

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,value):
        self.__year = value

    @property
    def maintanance(self):
        return self.__maintanance

    @maintanance.setter
    def maintanance(self,value):
        self.__maintanance = value

    def show_detail(self):
        super().show_detail()
        print('=== Car Detail ====')
        print(f'{self.barnd} with speed {self.speed} km/hr')
        print(f'manufacetered in {self.year}')

    def show_maintanance(self):
        print(f'The lastest maintanance in {self.maintanance}')




class Truck(Vehicle):
    def __init__(self, barnd, speed) -> None:
        super().__init__(barnd, speed)
        self._capacity = 1000
        self._wheel = 4

    @property
    def capacity (self):
        return self.__capacity 

    @capacity.setter
    def capacity (self,value):
        self.__capacity  = value

    @property
    def wheel  (self):
        return self.__wheel 

    @wheel .setter
    def wheel (self,value):
        self.__wheel  = value

    def show_detail(self):
        super().show_detail()
        print('=== Truck Detail ====')
        print(f'{self.barnd} with speed {self.speed} km/hr')
        print(f'carry {self.capacity} tons')

    def show_price(self):
        if self.wheels == 4:
            price = 1000
        elif self.wheels == 6:
            price = 1500
        elif self.wheels == 8:
            price = 2000
        else:
            price = 3000
        
        print(f'{self.wheels}wheel truck = {price} baht/day')

class Motocycle(Vehicle):
    def __init__(self, barnd, speed) -> None:
        super().__init__(barnd, speed)
        self.__cc = 150
        self.model = ''

    @property
    def cc (self):
        return self.__cc

    @cc.setter
    def cc(self,value):
        self.__cc = value

    @property
    def model (self):
        return self.__model

    @model.setter
    def model(self,value):
        self.__model = value

    def show_detail(self):
        super().show_detail()
        print('=== Motocycle Detail ====')
        print(f'{self.barnd} with speed {self.speed} km/hr')
        print(f'cc {self.cc} ')
