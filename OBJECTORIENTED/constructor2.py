# constructor overloading is not possible
class Stud:
    def __init__(self):
        print("no arg constructor")
    def __int__(self,name,age):
        print("two args")

obj = Stud()
obj = Stud("rif",25)
