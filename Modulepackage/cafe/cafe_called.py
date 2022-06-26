#วิธีที่ 1
from cafe_modlue import Drinks
from cafe_modlue import Desserts

desserts = Desserts()
print(desserts.show_desserts() )

#วิธีที่2

drinks = Drinks()
print(drinks.show_drink())
drinks.add_drink('สมูทตี้')
print(drinks.show_drink())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drink())