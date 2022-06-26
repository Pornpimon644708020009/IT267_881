#วิธีที่ 1
from secrets import choice
from tkinter import N
from measure import Measure    #called class เพราะประกาศตัวแปรเป็น Class 

if __name__=="__main__":
    mobj = Measure()
    #ให้ user เลือกได้ว่าต้องการแปลงเป็น inch หรือ cm
    choice = input('Choose menu (1: inch, 2: cm ):')
    #รับค่าตัวเลขจาก User ได้
    number = float(input('Enter number: '))

    if choice == '1' :
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch ')
    elif choice == '2':
        print(f'{number} = {mobj.inch_cm(number):.2f} cm ')
    else:
        print ('choose wrong menu')

    
    #วิธีใส่ค่าคงที่
    print(f'****** วิธีใส่ค่าคงที่ *********')
    print(f'5 Cm = {mobj.cm_inch(5):.2f} inch ')
    print(f'28.5 inch = {mobj.inch_cm(28.5):.2f} cm ')
