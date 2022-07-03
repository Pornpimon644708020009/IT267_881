from geographic import Geographic
from temperature import Temperature
#เป็น muilti inher เพราะมีมากกว่า 1 ตัว
class Country(Geographic,Temperature):    
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self) #inher intit จาก class geograph
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density (self):
        return self.population/self.area

    def show_detail(self):
        #ชื่อประเทศ
        print(f'Country : {self.name}')
        #สถานที่ lat,long
        print(self.getcordinate())  #ค่า lat,long
        
        #จำนวนพื้นที่ ประชากร ความหนาแน่น
        print(f'Area : {self.area}')
        print(f'Population : {self.population} Million')
        print(f'Density :{self.getpopulation_density()}.2f')

        #TimeZone,Climate,Temperature,Weather
        print(f'Timezone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Celsius(C) :{self.celsius}')
        print(f'Fahrenheit(F) :{self.getfahrenheit()}')
        print(f'Weather :{self.getweather()}')
        print()


