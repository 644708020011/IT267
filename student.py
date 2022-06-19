class Student: #ชื่อ class อักษรขึ้นต้นเป็นตัวใหญ๋

    def __init__(self,id:str,name:str,major:str):
        self.id = id
        self.name = name
        self.major = major

    def printdisplay_detail(self):
        print(f"id: {self.id}")
        print(f"Name: {self.name}")
        print(f"major: {self.major}")

if __name__=="__main__":
    Jessica = Student("111","Jessica","IT")    
    Jessica.printdisplay_detail()

    John = Student("112","John","MKT")    
    John.printdisplay_detail() #ใส่()ทุกครั้งหลังเรียกใช้

