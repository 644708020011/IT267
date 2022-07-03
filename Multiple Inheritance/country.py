from lib2to3.pgen2.token import RPAR
from geographic import Geographic
from temperture import Temperture

class Country(Geographic,Temperture):
    def __init__(self,name:str,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperture.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density (self):
        return self.population / self.area

    def show_detail (self):
        #ชื่อประเทศ
        print(f'Country Name: {self.name}')

        #สถานที่ตั้ง
        print(self.getcordinate)

        #แสดงขนาดพื้นที่
        print(f'Area : {self.area}')
        print(f'Population : {self.population} Million')
        print(f'Density : {self.getpopulation_density}')

        #timezone , cilmate , temperture , weather
        print(f'Timezone: {self.gettimezone}')
        print(f'cilmate{self.getcilmate}')
        print(f'Temperture(C): {self.celsius}')
        print(f'Temperture(F): {self.getfahrenheit()}')
        print(f'Weather:{self.getweather()}')
        print()

    
    
