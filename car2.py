class Car:
    brand = "Toyota"

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
#instance Method 
    def printCarDetail(self):
        print(f"Brand: {self.brand}") #เรียกจาก Class ใหญ่ได้ แต่ก็ต้องเรียกวัตถุตัวมันเองด้วย = self.Brand
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}") #ต้องการให้ค่าเป็นทศนิยม 2 แหน่ง

    #staticmethod ไม่มีคำว่า self
    @staticmethod
    def get_static_method(): 
        text = "Static"
        print(f"In {text} method") #ตัวแปร Text ไม่สามารถถูกเรียกใช้ใน printCarDetail()ได้

    #class method ต้องมี cls เสมอ
    @classmethod
    def get_class_method(cls):
        my_text = "Class"
        print (f"This is {my_text} method")

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    my_car = Car("Cross","white",2022,150000)
    my_car.printCarDetail()

    #เรียกใช้ static method
    Car.get_static_method() #เรียกผ่าน Class
    my_car.get_static_method() #เรียกผ่าน instance/object

    #เรียกใช้ class method
    Car.get_class_method() #เรียกผ่าน Class
    my_car.get_class_method() #เรียกผ่าน instance/object