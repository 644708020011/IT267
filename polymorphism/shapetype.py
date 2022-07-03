from shape import Shape
from math import pi

class Square(Shape):
    def __init__(self,length = 0) -> None:
        super().__init__()
        self.shape = 'Square'
        self.__length = length
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,value):
        self.__length = value
    
    def compute_area(self):
        super().compute_area()
        self.area = self.length **2

    def print_square(self):
        print(f'{self.shape} Area = {self.area:.2f}')



class Circle(Shape):
    def __init__(self,radius=0) -> None:
        super().__init__()
        self.shape = 'Circle'
        self.__radius = radius

    @property
    def radius(self):
        return self.__redius

    @radius.setter
    def radius(self,value):
        self.__radius = value

    def compute_area(self):
        super().compute_area()
        self.area  = pi * (self.radius ** 2)

    def print_circle(self):
        print(f'{self.shape} Area = {self.area:.2f}')

class Triangle(Shape):
    def __init__(self,base=0,high=0) -> None:
        super().__init__()
        self.shape = 'Triangle'
        self.__base = base
        self.__high = high

    @property #getter_base
    def base(self):
        return self.__base

    @base.setter  #setter_base
    def base(self,value):
        self.__base = value

    @property    #getter high
    def high(self):
        return self.__high

    @high.setter #setter high
    def high(Self,value):
        Self.__high = value

    def compute_area(self):
        super().compute_area()
        self.area = 0.5 * self.base * self.high
    
    def print_triangle(self):
        print(f'{self.shape} Area = {self.area:.2f}')



