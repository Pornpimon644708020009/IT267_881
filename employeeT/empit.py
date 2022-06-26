from employee import Employee

class EmpIT(Employee):      #เอาทุกอย่างในคลาสแม่เลย
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.deparment = 'IT'

    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,exp):
        self.experience = exp

    def emp_detail(self):
        print(f'skill:{self.skill}')
        print(f'experience : {self.experience}')

    def it_salary(self):
        self._emp_salary()
