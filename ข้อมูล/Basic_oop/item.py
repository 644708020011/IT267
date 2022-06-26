class Item:
    def __init__(self,name:str,price:float,quantity = 1) -> None:
        #ตรวจสอบ price,quantity ต้อง >0
        assert price > 0,f"Price {price} must greater than 0"
        assert quantity > 0,f"quantity {quantity} must greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

#instance method ต้องมีคำว่า self ต่อท้ายเสมอ
#การเรียก method ใช้ต้องมี การสร้า่ง object
    def total_price(self):  
        return self.price * self.quantity

    def __del__(self):
        print("Object was destory")

if __name__=="__main__":
    item1 = Item("Monitor",5600,2)
    item2 = Item("Wire",200,2)
    print("=== total Price ===")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")