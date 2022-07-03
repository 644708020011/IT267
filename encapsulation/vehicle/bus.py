from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, name: str, wheels: int, max: int, vin: int) -> None:
        Vehicle.__init__(self,name, wheels, max, vin)

    def set_color(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def v_detail(self):
        Vehicle.v_detail(self)
        print(f'Color:{self.color}')
        print(f'Capacity:{self.capacity}')

