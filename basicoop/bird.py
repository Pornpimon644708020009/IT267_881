class Bird:
    global bird_type #ถ้าไม่ใช่คำว่า global ตัวแปร bird_type จะกลายเป็น class variable
    bird_type = 'parrot'
    bird_name = 'Lori' #class variable

    def __init__(self,color) -> None:
        self.color = color #instance variable
        name = "Peter" # local variable
        print(f'{name} in init')

if __name__ == "__main__":
    my_bird = Bird('Green, Blue')

    #call instance variable ชื่อวัตถุ.instance variable
    print(my_bird.color)
    #call class variable ชื่อคลาส.instance variable
    print(ฺBird.bird_name)
    #call global variable เรียกชื่อตัวแปรได้เลย 
    print(bird_type)
