
from area import Area

area = Area()
area.base = float(input("Enter base: "))
area.high = float(input("Enter high: "))
print(f'Area = {area.computer_area():.2f}')