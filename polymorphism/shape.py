class Shape:
    def __init__(self,) -> None:
        self.__shape = None
        self.__area = 0

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape (self,value):
        self.__shape  = value

    @property
    def area(self):
        return self.__area

    @area.setter
    def area (self,value):
        self.__area = value

    def compute_area(Self): 
        pass
