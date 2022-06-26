class Person:
    def __init__(self,name:str,gender:str,profession:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0
    
    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.study = hours

    def show(self):
        print(f'Name: {self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.study}')

#Person1
jessa = Person('Jessa','Female','Software Engineer')
jessa.work()
jessa.show()

#Person2
john = Person('John','Male','Docter')
john.work()
john.study = 15 
john.show()

#Person3
Lisa = Person('Lisa','Female','Korean Singer')
Lisa.work()
Lisa.study = 10 
Lisa.show()



    
