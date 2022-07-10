
class Bi:
    def __init__(self) -> None:
        self.__buil = None

    @property
    def buil (self):
        return self.__buil

    @buil.setter
    def buil(self,value):
        self.value = value

    def print_detail (self):
        return self.buil

if __name__ == "__main__":
    o = Bi()
    o.buil = str(input("Enter word: "))
    o.print_detail()
