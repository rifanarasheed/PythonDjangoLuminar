# constructor --> another method to intialize instance variable in class
# constructor name always same as class name in java and c++
# In python we create constructor by __init__()
# constructor automatically invoked during object creation

class Student:                                                                           # class student created
    def __init__(self,name,roll,course):                                                 # constructor created with __init__()
        self.name = name                                                                 # intialization of instance variables
        self.roll = roll
        self.course = course
    def print_student(self):                                                             # another method created for printing
        print("name : ",self.name,", roll no : ",self.roll,", course :",self.course)     # instance variable can be accessed inside class by using self.variable

stud = Student("rif",100,"Django")                                                       # no need to add __init__() as it is invoked during object creation of that class, when student() is called,at that time constructor is invoked
stud.print_student()