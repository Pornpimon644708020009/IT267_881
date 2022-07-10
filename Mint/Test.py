
class Movie:
    def __init__(self) -> None:
        self._title = None
        self._year = None
        self._geane = None
        self._rating = None

    def _add_moive(self,title:str,year:str,geane:int):
        self._title = title
        self._year =year
        self._geane = geane

    def _get_movie_detail(self):
        print (f'Title : {self._title}')
        print (f'Year : {self._year}')
        print (f'Geane : {self._geane}')

    def print_detail(self):
        self._get_movie_detail

class Documentary(Movie):
    def __init__(self) -> None:
        super().__init__()

    def add_channel(self,ch):
        self.channel = ch

    def print_detail(self):
        super().print_detail()
        print (f'Channel : {self.channel}')
    

if __name__ == "__main__":
    m1 = Documentary()
    m1._add_moive("iom",2020,"comdy")
    m1._get_movie_detail()
    m1.add_channel("mint")
    m1.print_detail()
   


