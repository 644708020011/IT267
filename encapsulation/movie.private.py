class Movie:
    def __init__(self) -> None:
        #ตัวแปร private ขึ้นต้นด้วย undersore 2 ครั้ง
        self.__title = None
        self.__year = None
        self.__gener = None
        self.__rating = 5 

    # method protected ขึ้นต้นด้วย undersore 1 ครั้ง
    def _add_movie(self,title:str,year:int,gener:str,rating=5):
        self.__title = title
        self.__year = year
        self.__gener = gener
        self.__rating = rating


    def __getmovie_detail(self):
        print(f'Title:{self.__title}')
        print(f'Year:{self.__year}')
        print(f'Gener: {self.__gener}')
        print(f'Ranting: {self.__rating}')

    #สร้าง public method
    def print_detail(self):
        self.__getmovie_detail()

class Documenttary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)
        
    def add_channel(self,ch:str):
        self.channel = ch
    
    def print_detail(self):
        super().print_detail()
        print(f'Channel: {self.channel}')


    #make object
if __name__ == '__main__':
    m1 = Documenttary()
    m1._add_movie('My Octopus Teacher',2020,'Ducomentary')
    m1.add_channel('NetFlix')
    m1._Movie__getmovie_detail() #จะไม่มีข้อมูลของ channel (overriding method)
    #m1._Movie__getmovie_detail()
    m1.print_detail()
