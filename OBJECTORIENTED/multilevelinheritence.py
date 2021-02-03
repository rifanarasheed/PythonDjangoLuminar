# inheriting in different levels
# now subchild class will have all the features of child class and parent class as

class Parent:
    def m1(self):
        print("inside parent1")
class Child(Parent):
    def m2(self):
        print("inside child")
class Subchild(Child):
    def m3(self):
        print("inside subchild")

obj = Subchild()
obj.m3()
obj.m2()
obj.m1()