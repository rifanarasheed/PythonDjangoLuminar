# nested dictionary

employee = {
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"jerry","salary":20000,"exp":2},
    1002:{"id":1002,"name":"raj","salary":30000,"exp":2},
    1003:{"id":1003,"name":"rahul","salary":35000,"exp":3},
}

# nested dictionary
print(employee[1000])    # first will check whether key = 1000 is present or not, then prints its value

# print name of employee who have id = 1001
# first we need to check whether that key,ie,id is present or not in employee dict
# if that id is present then need to print name by its key [firstdictkey][seconddictkey]
if 1001 in employee:
    print(employee[1001]["name"])
else:
    print("employee with id does not exist")

# print salary of 1003
if 1003 in employee:
    print(employee[1003]["salary"])
else:
    print("employee with id does not exist")

# we can do this by creating a method also
# to print name of the employee with id 1000
# if no id is passed,"employee with id does not exist" will be printed as nothing is passed
def print_employee(id=None):
    if id in employee:
        print(employee[id]["name"])
    else:
        print("employee with id does not exist")

print_employee(id=1000)

# now we want to pass multiple arguments to the method in the form of key and value
# if we want to pass arguments normally, argument list will be same length as parameter
# def print_employee(id=None,prop=None)
# to avoid that and to sent as much as argument, we use *kwargs
# in dictionary format
# id is mandatory field
def print_employee(**kwargs):
    # print(kwargs)                   # kwargs = {'id': 1002, 'property': 'salary'}
    # to fetch id from kwargs
    id = kwargs["id"]                 # id = 1002
    if id in employee:                # if id is present or not (id is mandatory as it is the outer dictionary)
        print(employee[id]["name"])   # prints name of employee corresponding to id
        if "prop" in kwargs:          # if prop is present in kwargs
            prop = kwargs["prop"]     # fetching prop from kwargs ,ie,salary
            print(employee[id][prop]) # prints salary with corresponding id
        else:
            pass                       # if no prop is given, it is passed.
    else:
        print("employee with id does not exist")

print_employee(id=1002,prop="salary")     # any property should be printed with id as identification

# to print experience with keyword arguments method
def print_employee(**kwargs):              # kwargs = {'id': 1002, 'property': 'exp'}
    id = kwargs["id"]                      # fetching id from kwargs
    if id in employee:                     # if id is present dictionary
        print(employee[id]["name"])        # printing its employee name
        if "prop" in kwargs:               # if prop is present in kwargs or not
            prop = kwargs["prop"]          # fetching prop from kwargs to prop,ie, exp
            print(employee[id][prop])      # printing the prop,ie, exp of that id
        else:                              # if no prop is passed, pass
            pass
    else:
        print("employee doesnot exist")

print_employee(id=1002, prop="exp")

# by prop, we can pass any key to display its value



