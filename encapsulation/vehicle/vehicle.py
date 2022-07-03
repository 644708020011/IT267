class Vehicle:
    def __init__(self,name:str,wheels:int,max:int,vin:int) -> None:
        self.name=name
        self.wheels=wheels
        self._max_speed = max
        self.__vin = vin

    def set_vin(self):
        self.__vin = vin 
        

    def v_detail(self):
        print('==================')
        print(f'Name: {self.name}')
        print('==================')
        print(f'Wheels: {self.wheels}')
        print('==================')
        print(f'Max_speed:{self._max_speed}')
        print('==================')
        print(f'Vin:{self.__vin}')
        print('==================')