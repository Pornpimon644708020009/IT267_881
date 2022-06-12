class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study
    
    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def show(self):
        print(f'Name: {self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.study}')

#Person1
jessa = Person('Jessa','Female','Software Engineer','0')
jessa.work()
jessa.show()

#Person2
john = Person('John','Male','Docter','15')
john.work()
john.show()

#Person3
Lisa = Person('Lisa','Female','Korean Singer','10')
Lisa.work()
Lisa.show()



    
