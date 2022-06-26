class Desserts:
    def __init__(self) -> None:
        self.desserts = ['ข้าวเหนียวมะม่วง','ข้าวเหนียวทุเรียน','ไอศครีม']  #โครงสร้างเป็น List เพื่อสามารถปรับแก้ได้
    
    def show_desserts (self):
        return f'Desserts Menu : {self.desserts}'

class Drinks:
    def __init__(self) -> None:
        self.drinks = ['กาแฟ','ชา','น้ำอัดลม','ไวน์']
    
    def add_desserts (self,new_drink):  #เพิ่ม Drink เข้าไปโดยใช้ .append
        self.drinks.append(new_drink)
        return f'Drinks Menu : {self.drinks}'

    def show_drinks (self):
        return f'Drinks Menu : {self.drinks}'

        