employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",25000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],
]

# print number of employees in this company
number_of_employees = len(employees)
print("number of employees : ",number_of_employees)

# print how amount to be raised for company to pay salary to employee
totalamount = 0
for emp in employees:
    totalamount+=emp[3]
print("total amount :",totalamount)

# group of designation
data_count = 0
ba_count = 0
developer_count = 0
for emp in employees:
    if emp[2]=="dataanalyst":
        data_count+=1
    elif emp[2]=="ba":
        ba_count+=1
    else:
        developer_count+=1
print("data analyst:",data_count)
print("business analyst:",ba_count)
print("developer :",developer_count)

# print highest payed employee
payed_list = []  # empty list to store salary
for emp in employees:
    payed_list.append(emp[3])
highsalary = max(payed_list)
for emp in employees:
    if (emp[3]==highsalary):
        print(emp)

# print employees whose salary is less with designation = developer
devel_payed_list = []
for emp in employees:
    if (emp[2]=="developer"):
        devel_payed_list.append(emp[3])
lowsalary = min(devel_payed_list)
for emp in employees:
    if (emp[3]==lowsalary):
        print(emp)