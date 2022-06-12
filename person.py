class Person:
    def __init__(self,name,gender,profession) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.study = hours
            
    def show(self):
        print(f'Name:{self.name} Gender:{self.gender} Profession: {self.profession} study: {self.study}')

#person 1
jessa = Person('Jessa' , 'Female' , 'software Engineer')
jessa.work()
jessa.show()

#person 2
jon = Person('Jon' , 'male' , 'Doctor' , )
jon.study (15)
jon.work()
jon.show()

#person
#lisa =
