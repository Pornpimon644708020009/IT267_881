class Horse:
    def __init__(self,name:str,color:str,max_height:float) -> None:
        self.name = name
        self.color = color
        self.max_height = max_height

    def run(self):
        print (f'{self.name} is running')

    def show_name(self):
        print (f'Name : {self.name}')

    def show_info(self):
        print (f'Name : {self.name}\nColor : {self.color}\nMax Height: {self.max_height}')

