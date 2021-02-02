# polymorphism --> more than one form
#   ex: human behaviour changes according to their situations
# method overloading
# method overriding
# operator overloading

# method overloading
# same method name with different number of argument
class Maths:
    def add(self):
        print("no args")
    def add(self,num1):
        print("one args")
    def add(self, num1,num2):
        print("two args")

m = Maths()
m.add(22)