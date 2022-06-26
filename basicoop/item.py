class Item :

    def __init__(self,name:str,price:float,quantity=1) -> None:
        #ตรวจสอบ price,quantity ต้องมากกว่า 0 โดยใช้คำสั่ง assert
        assert price > 0,f"Price {price} must greater than 0"
        assert quantity > 0, f"Quantity{quantity} must greater than 0" #ถ้าหากผ่านเงื่อนไขแล้วค่าก็จะไปจัดเก็บใน self ตัวมันเอง
        self.name = name
        self.price = price
        self.quantity = quantity

    #instance method ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ method ต้องมีการสร้าง object
    def total_price(self):
        return self.price * self.quantity 
        #self.total = self.price * self.quantity
        #return self.total (ใช้ได้เหมือนกัน)

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    item1 =Item("Moniter",5600)
    item2 =Item("Mouse",1500,2)
    print("=== Total Price ===")
    print(f"{item1.name} :{item1.total_price():,.2f}")
    print(f"{item2.name} :{item2.total_price():,.2f}")