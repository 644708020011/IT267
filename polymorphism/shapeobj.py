from shapetype import *
#import * หมายถึงเอาทั้งหมดใน class นั้น

print("====== คำนวณพื้นที่รูปทรงต่างๆ ======")
print("1) สี่เหลี่ยม")
print("2) วงกลม")
print("3) สามเหลี่ยม")
choice = int(input("เลือกพื้นที่ต้องการคำนวณ 1-3:"))
print("**************************")

if choice == 1:
    s = Square()
    s.length = float(input("Enter Length"))
    s.compute_area()
    ############
elif choice == 2:
    c = Circle()
    c.radius = float(input("Enter radius"))
    c.compute_area()

elif choice == 3:
    t = Triangle()
    t.base = float(input("Enter Base"))
    t.high = float(input("Enter High"))
    t.compute_area()

else:
    print("!!ใส่ตัวเลขผิด!!")