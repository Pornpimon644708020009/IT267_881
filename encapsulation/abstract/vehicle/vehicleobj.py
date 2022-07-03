from vehiclesubclass import *
#Car
c = Car("Mazda",250)
c.year = 2020
c.gear = 7
c.seat = 4
c.show_detail()
c.maintance = 2022
c.show_maintanance()

#Truck
t = Truck("IsuZu",120)
t.capacity = 1000
t.wheels = 4
t.show_detail ()
t.show_price()

#Motocycle
m = Motocycle("Honda",100)
m.cc = 160
m.model = "New PCX"
m.show_detail()