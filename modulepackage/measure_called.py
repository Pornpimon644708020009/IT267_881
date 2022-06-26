#วิธีที่ 1
from measure import Measure    #called class เพราะประกาศตัวแปรเป็น Class 

if __name__=="__main__":
    mobj = Measure()
    print(f'5 Cm = {mobj.cm_inch(5):.2f} inch ')
    print(f'28.5 inch = {mobj.inch_cm(28.5):.2f} cm ')
