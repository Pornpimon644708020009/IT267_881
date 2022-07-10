from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, name: str,color: str, max_height: float,age:int,weight:float) -> None:
        super().__init__(name, color, max_height)
        self.name = name
        self.color = color
        self.max_height = max_height
        self.age = age
        self.weight = weight

    def run(self):
        return Horse.run()

    def sound(self):
        return super().sound()

    def show_info(self):
        return super().show_info()


if __name__ =="__main__":
    print (f'*******Mumu Info *******')
    mule1 = Mule("Mumu","Blue-eyed cream","200","3","200")
    mule1.show_info()

    print (f'*******Meme Info *******')
    mule2 = Mule("Meme","Palomino","200","1","120.7")
    mule2.show_info()