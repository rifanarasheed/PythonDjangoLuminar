# inheriting from multiple class
# if m1() is called, child class m1() will be print because child class is given first before parenting in subchild()
# if the method m1() is not seen in child class, then only will check for m1() in parent class
# no method overloading

class Parent:
    def m1(self):
        print("inside parent1")

class Child(Parent):
    def m1(self):
        print("inside child m1")
    def m2(self):
        print("inside child m2")

class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

obj = Subchild()
obj.m3()
obj.m2()
obj.m1()