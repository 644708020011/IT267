from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, max_height:float,name:str,color:str,age:int,weight:int) -> None:
        #super().__init__(max_height, name, color)
        Horse. __init__(self)
        Donkey.__init__(self)
        self.max = max_height
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight

    def run(self):
        return super().run()


    def Show_info(self):
        print(f'***** {self.name} inof *****')
        print (f'Name:{self.name}')
        print (f'Color:{self.color}')
        print (f'Max Height" {self.max}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight}')

