from Bank.customer import Customer
from Bank.account import Account

#สร้าง obj #ไม่ว่าจะใส่ชื่ออะไรก็จะเปลี่ยนตาม
Paul = Customer()
Paul.new_customer()

#สร้าง obj account
Paul_acc = Account()
Paul_acc.open_account(Paul.name,'Saving','0123-4578','500')

#แสดงข้อมูลของ Customer paul
print(Paul.cus_info())

#แสดงข้อมูลเงินคงเหลือ
print(Paul_acc.display_balance())