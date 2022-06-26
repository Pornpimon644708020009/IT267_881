from tkinter import E
from empit import EmpIT

mike = EmpIT('001','Mike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

from empmkt import EmpMKT
anna = EmpMKT('002','Anna',35000)
anna.emp_detail()
anna.mkt_salary()

jess = EmpMKT('003','jess',45000)
jess.add_location('ChiangMai')
jess.add_commission(35)
jess.emp_detail()
jess.mkt_salary()