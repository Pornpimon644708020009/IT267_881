class Car:
    brand = "Toyota"

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def printCarDetail(self):
        print(f"Brand: {self.brand}") #เรียกจาก Class ใหญ่ได้ แต่ก็ต้องเรียกวัตถุตัวมันเองด้วย = self.Brand
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}") #ต้องการให้ค่าเป็นทศนิยม 2 แหน่ง

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    my_car = Car("Cross","white",2022,150000)
    my_car.printCarDetail()