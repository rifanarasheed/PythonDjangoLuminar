class Student:                                                                           # class student created
    def set_student(self,name,roll,course):                                              # method set_student created with attributes name,roll,course
        self.name = name                                                                 # intialization of instance variables
        self.roll = roll
        self.course = course
    def print_student(self):                                                             # another method created for printing
        print("name : ",self.name,", roll no : ",self.roll,", course :",self.course)     # instance variable can be accessed inside class by using self.variable

stud = Student()                                                                         # stud is the object reference for student class
stud.set_student("rif",11,"Django")                                                      # calling methods of student class using its object reference
stud.print_student()

# print(obj.course)                                                                      # instance variable can be accessed outside class by using object reference of that class .
# print(obj.roll)
