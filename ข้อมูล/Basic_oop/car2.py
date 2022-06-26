from cgitb import text


class Car:
    brand = "Toyota"

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
    #instance method 
    def printCarDetail(self):
        print(f"Brand: {self.brand} ")
        print(f"Model: {self.model} ")
        print(f"Colour: {self.colour} ")
        print(f"Year: {self.year} ")
        print(f"Price: {self.price:,.2f} ")

#staticmethod ไม่มีคำว่า slef
    @staticmethod
    def get_static_method():
        text = "static"
        print(f"im {text} method")

# class method ต้องมี cls
    @classmethod
    def get_class_method(cls):
        my_text = "class"
        print(f"this is (my_text) method")

    def __del__(self):
        print("Object was destroy")

if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()  

    #เรียกใช้ static midthod
    Car.get_static_method() #เรียกผ่าน static
    my_car.get_static_method()

    #เรียกใช้ class method
    Car.get_class_method() #เรียกผ่าน class
    my_car.get_class_method()