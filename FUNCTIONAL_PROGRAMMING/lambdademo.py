# functional programming means optimising the function or method into small format
# normal method defining
def add(num1,num2):
    return num1+num2

# remove return, bring everything into one line,
# then remove def and method name and method bracket and assign into one variable
# call that variable with arguments to pass

# lambda function should be in single line
add = lambda num1,num2:num1+num2

cube = lambda num:num*num*num        # num**3
print(cube(2))

even = lambda num:num%2==0
print(even(20))