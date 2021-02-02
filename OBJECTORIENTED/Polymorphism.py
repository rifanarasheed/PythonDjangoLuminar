# polymorphism --> more than one form
#   ex: human behaviour changes according to their situations
# method overloading
# method overriding
# operator overloading

# method overloading
# same method name with different number of argument
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
m.add(34)                 # throws error