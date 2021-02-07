# number of input values has corresponding output values
# ex : converting lowercase letter into uppercase letter

lst = [1,2,3,4,5,6]

# normal method to do square root of numbers
def square(num):
    return num**2

# normal way to print values of square
sqlst = []
for i in lst:
    sqlst.append(square(i))
print("listing :",sqlst)

# instead of doing this way, we go for map()
# map function has two parameters :
# one is function to indicates which function to map
# next parameter is iterables to indicate on which we need iteration  like list,tuple,set,dictionary.
#            map(function,iterables)
sqlist = list(map(square,lst))                   # we need output in the form of list, converting into list
print("mapping using normal method :",sqlist)

# or we can do square in lambda function to concise the code more :
sqlist1 = list(map(lambda num:num**2,lst))
print("mapping using lambda method :",sqlist1)









