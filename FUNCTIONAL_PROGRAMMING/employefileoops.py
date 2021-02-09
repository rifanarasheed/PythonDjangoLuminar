# combining oops,files,list with reduce,filter and map

# print employee details whose designation developer --> filter()
# no of employees as developer --> filter()
# print employee details who have highest salary -->map
# # to print employee whose is having highest and lowest salary with designation = developer -->reduce

# now the text file does not have any format(string),so each line of text file need to make as each object of a class
# first create a class to intialize instance variable

from functools import reduce

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
    emplist.append(Employee(eid,ename,edesign,exp,salary))                    # creating objects and appending them into emplist (obj = Employee(eid,ename,edesign,exp,salary), we dont need to specify obj here)
print(emplist)

# print employee details whose designation = developer
devop = list(filter(lambda emp: emp.edesign=="developer",emplist))
for dev in devop:
    print(dev)

# print number of developers in employee list
count = len(list(filter(lambda emp: emp.edesign=="developer",emplist)))       #  count = len(devop)  -->if we have list of developer exclusively
print(count)


# print employee details who have highest salary
#sallist = []
#for employee in emplist:
#    sallist.append(employee.salary)                          # appending the salary
#print(sallist)
#highsal = max(sallist)                                       # using max function to get the highest salary
#for emp in emplist:
#    if emp.salary == highsal:
#        print("high salary : ",emp)

# instead of doing this codes, we can concise code by functional programming

highsal = max(list(map(lambda emp:emp.salary,emplist)))       # using map() to get salary of employee in a list and finding max number from list. all in one single line using lambda and map()
print(highsal)


# to print employee whose is having highest and lowest salary with designation = developer
devlist = []
for employee in emplist:
    if employee.edesign == "developer":
        devlist.append(employee.salary)
print(devlist)
#dev_low_sal = min(devlist)
#for emp in emplist:
#    if emp.edesign == "developer":
#        if emp.salary == dev_low_sal:
#            print("developer with low salary :",emp)

dev_highsal = reduce(lambda no1,no2: no1 if no1>no2 else no2,devlist)
print(dev_highsal)

dev_lowsal = reduce(lambda no1,no2: no1 if no1<no2 else no2,devlist)
print(dev_lowsal)










