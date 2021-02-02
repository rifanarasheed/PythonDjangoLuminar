# constructor overloading is not supported, ie , more than  one constructor --> __init__()\
# the constructor which is implemented recently will be executed, not the previous ones
# in the below example, the constructor with the arguments will be implemented as it is recent one
class Stud:
    def __init__(self):
        print("no arg constructor")
    def __int__(self,name,age):
        print("two args")

obj = Stud()
obj = Stud("rif",25)
