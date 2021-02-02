class Employee:
    def set_employee(self,Eid,Ename,Edesignation,Esalary):
        self.Eid = Eid
        self.Ename = Ename
        self.Edesignation = Edesignation
        self.Esalary = Esalary
    def print_employee(self):
        print("Employee ID :",self.Eid)
        print("Employee name :",self.Ename)
        print("employee Designation :",self.Edesignation)
        print("Employee Salary :",self.Esalary)

emp = Employee()
emp.set_employee(1000,"rif","Developer",25000)
emp.print_employee()
# print(emp.Eid)
# print(emo.Ename)

emp1 = Employee()
emp1.set_employee(1001,"riya","Designer",30000)
emp1.print_employee()
# print(emp1.Eid)
# print(emp1.Ename)