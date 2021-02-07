# polymorphism --> more than one form
#   ex: human behaviour changes according to their situations
# method overloading
# method overriding
# operator overloading

# method overloading
# same method name with different number of argument in same class
# recently implemented method will only work.
# if only one argument is given, it will throw an error because last implemeneted method add() has two args passed

class Maths:
    def add(self):
        print("no args")
    def add(self,num1):
        print("one args")
    def add(self, num1,num2):
        print("two args")

m = Maths()
m.add(22,33)
#m.add(34)                 # throws error

# method overriding
# same method name with different number of arguments in different class
# in below example, if child class doesnt want to inherit mobile() of parent class,
# then it can define its own method.so that method of parent class will not be executed
# so mobile method of child class overrides mobile method of parent class.
# if no invoked method exist in child class then automatically take from parent class
class Parent:
    def mobile(self):
        print("nokia")
class Child(Parent):
    def mobile(self):
        print("iphone11")

c=Child()
c.mobile()

# Operator overloading
class Book:
    def __init__(self,pages):
        self.pages = pages
        print(self.pages)
    def __str__(self):
        print("printing object")
        return str(self.pages)

              #  100   200
              #  300    300
    def __add__(self, other):
        print("adding obj+ob1+obj2")
        # other is default attribute of __add__() which is same like self, thats why other.pages is given,same like intializing instance variable.
        return Book(self.pages+other.pages)          # 100 + 200 = (300), returns book type. then 300 + 300 = 600 0f book type

    def __sub__(self, other):
        print("subtracting obj-obj1")
        return Book(self.pages-other.pages)

    def __mul__(self, other):
        print("multiplying obj*obj2")
        return Book(self.pages+other.pages)

obj = Book(100)                       # constructor invoked, 100 will be passed to __init__()
obj1 = Book(200)                      # constructor invoked, 200 will be passed to __init__()
obj2 = Book(300)                      # constructor invoked, 300 will be passed to __init__()

# this below prints hexadecimal value object by invoking __str__() method of object class. we can do method overiding of __str__() in Book class(child class of Object class)
# __str__() can return only string values
# ex: pages are integer value (100), so to return them we need to convert them into string
print(obj)                             # first, the statement is to print obj,so __str__() will be invoked,
                                       # obj is the reference object of Book class,so 100 will be passed, pages = 100,then self.pages = 100
                                       # and return 100 as in __str__()

# we can use operator between integer or string but not between classes
# to do operations between classes, we go for OPERATOR OVERLOADING.
print(obj+obj1+obj2)                   # first by seeing the operator sign,__add__() (object class method overiding) will be invoked
                                       # first 100(obj) will be passed,so self.pages = 100,
                                       # to attribute other of __add__(), 200(obj1) will be passed,so pages = 200 and they get added and returns 300
                                       # but now self.pages = 300 and it is a integer type, and we cannot add int and class together,
                                       # so when returning it throws error, so we can make returning value as class type, ie, book type in this.
                                       # after that we came accross + again, so __add__() will be invoked.
                                       # to attribute other, 300(obj2) will be passed to pages, and returns added value, ie,300+300 =600,
                                       # then __str__() is invoked and returns self.pages currently value to print functiongi
                                       # by this way we can pass any number of arguments.

print(obj1-obj)

print(obj1*obj2)

