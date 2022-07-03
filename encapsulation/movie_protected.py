class Movie:
    def __init__(self) -> None:
        #ตัวแปร protected ขึ้นต้นด้วย undersore 1 ครั้ง
        self._title = None
        self._year = None
        self._gener = None

    # method protected ขึ้นต้นด้วย undersore 1 ครั้ง
    def _add_movie(self,title:str,year:int,gener:str):
        self._title = title
        self._year = year
        self._gener = gener

    
    def _getmovie_detail(self):
        print(f'Title:{self._title}')
        print(f'Year:{self._year}')
        print(f'Gener: {self._gener}')

#class Movie แลพ class Documentary อยู่ในไฟล์เดียวกันจึงไม่ต้อง import
class Documenttary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)
        
    def add_channel(self,ch:str):
        self.channel = ch

    def _getmovie_detail(self):
        Movie._getmovie_detail(self)
        print(f'channel:{self.channel}')        

    #make object
if __name__ == '__main__':
    m1 = Documenttary()
    m1._add_movie('My Octopus Teacher',2020,'Ducomentary')
    m1.add_channel('NetFlix')
    m1._getmovie_detail() #จะไม่มีข้อมูลของ channel (overriding method)
