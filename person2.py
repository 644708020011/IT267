class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')
          
    def show(self):
        print(f'Name:{self.name} Gender:{self.gender} Profession: {self.profession} study: {self.study}')

#person 1
jessa = Person('Jessa' , 'Female' , 'software Engineer', 0 )
jessa.work()
jessa.show()

#person 2
jon = Person('Jon' , 'Male' , 'Doctor' , 15 )
jon.work()
jon.show()

#person
lisa = Person('Lalisa' , 'FEmale' , 'Koren Singer' )
lisa.work()
lisa.show()