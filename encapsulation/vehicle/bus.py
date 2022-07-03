from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, name, wheels, max, vin) -> None:
        Vehicle.__init__(self,name, wheels, max, vin)

    def set_color (self,color):
        self.color = color

    def set_caparcity (self,caparcity):
        self.caparcity = caparcity

    def v_detail(self):
        Vehicle.v_detail(self)
        print(f'Color : {self.color}')
        print(f'Caparcity : {self.caparcity}')