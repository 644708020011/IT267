#from ชื่อของ package. ชื่อ module import ชื่อ class
from bank.customer import Customer
from bank.account import Account 


User = Customer()
User.new_customer()

new_use = Account()
new_use.open_account(User.Name,'saveing','095-2134123',500)

#แสดงผล ชื่อ ที่อยู่ เบอร์โทร
print(User.cus_info())
print(new_use.display_balance())


