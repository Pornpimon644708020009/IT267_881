class Movie:
    def __init__(self) -> None:
        #ตัวแปร private ขึ้นต้นด้วย __ 2 ครั้ง
        self.__title = None 
        self.__year = None
        self.__genre = None
        self.__rating = 5

    def _add_movie (self,title:str,year:int,genre:str,rating=5):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__rating = rating

    def __getmovie_detail(self):
        print(f'Title: {self.__title}')
        print(f'Year: {self.__year}')
        print(f'Genre: {self.__genre}')
        print(f'Rating: {self.__rating}')

    #สร้าง Puplic method เพื่อให้class อื่นใช้ Private method 
    def print_detail(self):
        self.__getmovie_detail

class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)

    def add_channel(self,ch:str):  #ถ้ามี type ก็ต้องใส่ 
        self.channel = ch

    def print_detail(self):  #Overlive
        super().print_detail()
        print (f'Channel : {self.channel}')

#สร้าง Obj 
if __name__=='__main__':
    m1 = Documentary()
    m1._add_movie('My Octopus Teacter',2020,'Documentary')
    m1.add_channel('NetFlix')
    #ถ้าจะใช้ Private method ต้องเรียกผ่าน Class mom โดยตรง เรียก private method : _className__privtenethod()
    #m1._Movie__getmovie_detail()
    m1.print_detail()