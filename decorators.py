# decorator are very usefull tool in python which allows the programmer to modify the function or class
# without actually effecting the function permanently
# that is the features which we would like to add can be given in by creating another function and declaring it as decorator right above the function which we would to add the feature.

"""
def sub(num1,num2):
    if num1>num2:
        (num1,num2)=(num2,num1)       # swapping number if num1 is less than num2
    return num1-num2

print(sub(10,20))

"""


def subtract(func):
    def inner(num1,num2):
        if num1 < num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return inner()

@subtract                                 # declaring decorator function
def sub(num1,num2):
    return num1-num2

data = sub(10,20)
print(data)