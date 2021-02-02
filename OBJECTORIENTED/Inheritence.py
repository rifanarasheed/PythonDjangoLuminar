class Parent:
    def phone(self):
        print(" i have phone ")

class Child(Parent):                    # inheriting from parent class
    pass

c = Child()
c.phone()

# print(c)    # prints hexadecimal value of object's location
# print(type(c)  # prints class child as c is the object of class child
# print(id(c)     # gives location id of object of class child