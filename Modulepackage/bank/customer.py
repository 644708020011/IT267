from ast import Return


class Customer:
    def __init__(self) -> None:
        self.Name = ''
        self.Address = ''
        self.Phone = ''

    def new_customer(self):
        self.Name = input('Enter name')
        self.Address = input('Enter youraddess')
        self.Phone = input('Enter your number phone')

    def cus_info(self):
        return f'name: {self.Name}\n address:{self.Address}\n phone{self.Phone}'
