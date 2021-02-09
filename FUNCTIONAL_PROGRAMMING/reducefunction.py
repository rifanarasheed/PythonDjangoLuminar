# number of input values generates a single value
# sum of three number

# reduce() is not readily available like map and filter
# we need to import them from package known as functools
# reduce() only accept number values

from functools import reduce

lst = [10,11,12,13,14]

def sum(num1,num2):                            # 10,11  21,12  33,13.....
    return num1+num2                           # 21     33      46

sum1 = reduce(sum,lst)
print("with method : ",sum1)

# with lambda function
sum = reduce(lambda num1,num2:num1+num2,lst)
print("with lamda function : ",sum)