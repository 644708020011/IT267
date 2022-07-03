from vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, name: str, wheels: int, max: int, vin: int) -> None:
        Vehicle.__init__(self,name, wheels, max, vin)

    def set_cc (self,cc):
        self.cc= cc
        
    def v_detail(self):
        Vehicle.v_detail(self)
        print(f'CC:{self.cc}')



