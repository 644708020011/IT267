class Donkey:
    def type_(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print (f'Donkey make eeyore sound')

    def show_info(self):
        print (f'Age: {self.age}')
        print (f'Weight: {self.weight}')
