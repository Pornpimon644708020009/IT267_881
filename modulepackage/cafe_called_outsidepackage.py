#วิธีเรียกที่ 1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks  #กรณีไฟล์อยู่ นอก Package ก็ต้องเรียก cafe.cafe_module
#วิธีเรียกที่ 2
#from cafe_module import Desserts,Drinks

desserts = Desserts()  #dessert เป็น obj โดยเรียกใช้งาน class Desserts
print(desserts.show_desserts()) 

drink = Drinks()
print (drink.show_drinks())
drink.add_desserts('สมูทตี้')  #เพิ่มเมนูเข้าไป
print(drink.show_drinks())
drink.add_desserts('น้ำมะพร้าว')  #เพิ่มเมนูเข้าไป
print(drink.show_drinks())

