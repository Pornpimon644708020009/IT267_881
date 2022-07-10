class C:
    def __init__(self,name:str) -> None:
        self.name = name
        #self.color = color

    def fav(self):
        print(f"FAV:KinPo")

    def print_detail (self):
        return (f'Name : {self.name}')

if __name__ == "__main__":
    m = C("Mint")
    choice = input('Choose menu (1: Go, 2: Nope ):') 
    #number = float(input('Enter number: '))

    if choice == '1' :
        print(f'love you')
    else:
        print (f'Bye Goodluck!')


