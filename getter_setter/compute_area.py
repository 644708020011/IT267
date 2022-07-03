from area import Arae
area = Arae()
area.base = float(input("Enter base: "))
area.high = float(input("Enter high: "))
print (f'Area = {area.compute_area():.2f}')