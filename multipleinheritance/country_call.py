import imp
from country import Country

c1 = Country('Thailand',513120,66.93)
c1.setcordinate(15.8700,100.9925)
c1.setcelsius(31) #ควรเรียกผ่านmethod ไม่ควรเรียกผ่าน attibute โดยตรง
c1.show_detail()

c2 = Country('Norway',385207,5.379)
c1.setcordinate(60.4720,8.4689)
c1.setcelsius(15) 
c1.show_detail()