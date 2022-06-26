from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.locarion = 'Bangkok'
        self.comision = 30
        self.department = 'Marketing'

    def add_location(self,location:str):
        self.locarion = location

    def add_comision(self,comision:int):
        self.comision = comision
    
    def emp_detail(self):
        super().emp_detail()
        print(f'location: {self.locarion}')
        print(f'comision: {self.comision} %')

    def mkt_salary(self):
        self._emp_salary()

