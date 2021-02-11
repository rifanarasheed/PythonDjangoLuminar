# to find square root of a number

lst = [10,20,30,40]

# 1. normal methoding
#def square(num):
#    return num**2
#for num in lst:
#    print(square(num))

# 2. functional programming using map and lambda
# square = list(map(lambda num:num**2,lst))

# 3. functional programming using list comprehension:
square = [num**2 for num in lst]                          # output in the form of list
print(square)