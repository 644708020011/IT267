class Desserts:
    def __init__(self) -> None:
        self.desserts = ['ข้าวเหนียวมะม่วง','ข้าวเหนียวทุเรียน','ไอศกรีม']

    def show_desserts(self):
        return f'Desserts Menu: {self.desserts}'

class Drinks:
    def __init__(self) -> None:
        self.drinks = ['กาแฟ','ชา','น้ำอัดลม','ไวน์']

    def add_drink(self,new_drink):
        self.drinks.append(new_drink)

    def show_drink(self):
        return f'drinks Menu: {self.drinks}'
