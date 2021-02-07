# combining oops,files,list

# print employee details whose designation developer
# no of employees as developer
# print employee details who have highest salary

# now the text file does not have any format(string),so each line of text file need to make as each object of a class
# first create a class to intialize instance variable

class Employee:
    def __init__(self,eid,ename,edesign,exp,salary):
        self.eid = eid
        self.ename = ename
        self.edesign = edesign
        self.exp = exp
        self.salary = salary
    def __str__(self):
        return self.ename

# opening the file to do operation
f = open("employeetextfile","r")

# creating empty list which is used to append objects to do operations after object creation of the class
emplist = []

for lines in f:
    #1000,anil,developer,3,35000\n
    eid,ename,edesign,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,ename,edesign,exp,salary))                 # creating objects and appending them into emplist (obj = Employee(eid,ename,edesign,exp,salary), we dont need to specify obj here)
print(emplist)

# to print name of the employee
for emp in emplist:
   print(emp)

# print employee details whose designation developer
for emp in emplist:
    if emp.edesign == "developer":
        print(emp)

# print employee details who have highest salary
sallist = []
for employee in emplist:
    sallist.append(employee.salary)                          # appending the salary
print(sallist)
highsal = max(sallist)                                       # using max function to get the highest salary
for emp in emplist:
    if emp.salary == highsal:
        print("high salary : ",emp)

# to print employee whose is having lowest salary with designation = developer
devlist = []
for employee in emplist:
    if employee.edesign == "developer":
        devlist.append(employee.salary)
print(devlist)
dev_low_sal = min(devlist)
for emp in emplist:
    if emp.edesign == "developer":
        if emp.salary == dev_low_sal:
            print("developer with low salary :",emp)









