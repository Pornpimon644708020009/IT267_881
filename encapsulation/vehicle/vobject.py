#object Bus
from bus import Bus

b1 = Bus("Volvo",4,120,"v123")
b1.setcolor("White")
b1.set_caparcity(34)
b1.v_detail()

#object motocycle
from motocycle import Motocycle
m1 = Motocycle("Honda",2,120,"VI18")
m1.set_cc(1200)
m1.v_detail()
m1.set_vin("VI18")
m1.v_detail()