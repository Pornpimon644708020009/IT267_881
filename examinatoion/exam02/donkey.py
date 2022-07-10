class Donkey:
    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound (self):
        print (f"Donky makes eeyore sound")

    def show_info(self):
        print (f'Age :{self.age}-year-old\nWeight : {self.weight}kg')

