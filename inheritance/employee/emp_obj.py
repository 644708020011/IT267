from emp_it import EmpIT

print('\n')
mike = EmpIT('001','mike',60000)
mike.add_Skill('Python,javascript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

print('\n')

from emp_mkt import EmpMKT
anna = EmpMKT('002','anna',35000)
anna.emp_detail()
anna._emp_salary()

print('\n')

jess = EmpMKT('003','jess',45000)
jess.add_location('Chiang Mai')
jess.add_comision(35)
jess.emp_detail()
jess._emp_salary()