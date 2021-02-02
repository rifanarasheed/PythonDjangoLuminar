# class --> plan, design pattern, blueprint,template
# object --> real world entity
# reference --> to perform operations on the object created
# eg : class : TV
#      object: samsung,sony

class Person:
    # creating methods
    def set_person(self,age,name):
        self.age = age
        self.name = name
    def print_person(self):
        print("name :",self.name)
        print("age :",self.age)

obj = Person()
obj.set_person(25,"niya")
obj.print_person()

# here first we created a class known as person()
# self is used to point to the class
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
# then created two methods known as set_person() as well as print_person
# we are not passing any arguments in print_person becuase that method is used for printing.no additional operation

# in set_person() :
#     intialization of instance variable.
#     instance variable are created with self keyword..ex: self.variable

# obj is the object created for class person() as a reference to do specific operation on methods or class.

# self.age and self.name are instance variables
# instance variable can be accessed outside class by using object reference of that class .
# instance variable can be accessed inside class by using self.variable



