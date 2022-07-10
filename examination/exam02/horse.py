class Horse:

    def type(self,max_height:float,name:str,color:str) -> None:
        self.max = max_height
        self.name = name
        self.color = color

    def run(self):
        print (f'{self.name} is running')


    def show_name(self):
        print (f'Name: {self.name}')

    def Show_info(self):
        print (f'Name:{self.name}')
        print (f'Color:{self.color}')
        print (f'Max Height" {self.max}')
