employee = {"id":1,"name":"rahul","experience":2,"salary":35000}

# to check whether key called "salary" present in the set employee
# if yes, print employee's salary
if("salary" in employee):
    print(employee["salary"])

# to print employee name
print(employee["name"])

# to check whether key known as gender is present in set
# if no, create key "gender" with value male
if("gender" in employee):
    print("exist")
else:
    employee["gender"] = "male"
print(employee)

# if any employee salary is <35000, add 5000rs more
if(employee["salary"]<=35000):
    employee["salary"]+=5000
print(employee)
