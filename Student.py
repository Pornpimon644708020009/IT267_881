class Student:

    def __init__(self,id:str,name:str,major:str) -> None:
        self.id = id
        self.name = name
        self.major = major
       
    def printdisplay_detail(self):
        print(f"ID: {self.id}")
        print(f"Name:{self.name}")
        print(f"Major:{self.major}")

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    Jess = Student("111","Jessica","IT")
    Jess.printdisplay_detail()

    John = Student("112","John","MKT")
    John.printdisplay_detail()
