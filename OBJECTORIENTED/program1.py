class Student:
    def __init__(self,id,name,course,total):
        self.id = id
        self.name = name
        self.course = course
        self.total = total
    def __str__(self):                          # this method only return string, no operation can be done
        return self.name

obj = Student(100,"akshay","Django",140)
obj1 = Student(101,"rekha","Mean",142)
obj2 = Student(102,"laila","Django",144)

# to print name of students who are doing "Django"
# creating empty list
# appending all objects into the list
studlist = []
studlist.append(obj)
studlist.append(obj1)
studlist.append(obj2)

for stud in studlist:
    if stud.course=="Django":
        print(stud.name)

# print total of django students
total = 0
for stud in studlist:
    if stud.course=="Django":
        total = total+stud.total
print(total)


