from pyclbr import Class

class Movie:
    def __init__(self) -> None:
        #ตัวแปร protected ขึ้นต้นด้วย _ 1 ครั้ง
        self._title = None #None meaning nothing data 
        self._year = None
        self._genre = None

    def _add_movie (self,title,year,genre):
        self._title = title
        self._year = year
        self._genre = genre

    def _getmovie_detail(self):
        print(f'Title: {self._title}')
        print(f'Year: {self._year}')
        print(f'Genre: {self._genre}')

class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)   #เรียก class มาใช้ อย่าลืม self

    def add_channel(self,ch:str):  #ถ้ามี type ก็ต้องใส่ 
        self.channel = ch

    def _getmovie_detail(self):
        Movie._getmovie_detail(self)
        print(f'Channel:{self.channel}')

#สร้าง obj
if __name__=='__main__':
    m1 = Documentary()
    m1._add_movie('My Octopus Teacter',2020,'Documentary')
    m1.add_channel('NetFlix')
    m1._getmovie_detail()  #เรียกใช้ของ Documentary (overridding method)

