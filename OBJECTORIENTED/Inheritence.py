# inheritence -> inheriting features of parent class  to child class
# parent -> child
# super -> sub
# base  -> derived

# single inheritence
class Parent:                           # class Parent(Object): is same
    def phone(self):
        print(" i have phone ")

class Child(Parent):                    # inheriting from parent class
    pass

c = Child()
c.phone()

# printing object
# print(c)    # prints an object while invoking __str__() method from object class.
# print(type(c)  # prints class child as c is the object of class child
# print(id(c)     # gives location id of object of class child

# object class is the default base(parent) class of every class defined
# so the methods present in the object class will be inherited to the child classes of object class which is basically every class.
# if we dont want to print statements given in the __str__() of object class(Parent class),
# then we can create our own statements to print by define __str__() in child class --> which is method overriding and inhertience(inheriting method from object class)
