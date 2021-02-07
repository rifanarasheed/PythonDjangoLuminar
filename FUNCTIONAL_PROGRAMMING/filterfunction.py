# number of input values is not equal to number output values
# ex: to find even number from a list
# conditions will be used

# to print even number of a list
lst = [1,2,3,4,5,6,7,8,9,10]

def even(num):
    if num%2==0:
        return num
#               filter(function,iterable)
evem_lst1 = list(filter(even,lst))

# or use lambda function to concise more

even_lst = list(filter(lambda num:num%2==0,lst))
print(even_lst)

# to print odd number of a list
odd_lst = list(filter(lambda num: num%2!=0,lst))
print(odd_lst)