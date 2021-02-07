from functools import reduce

lst = [10,11,12,13,14]

# to find highest number from the list
# high = max(lst)

# difference in max() and reduce()

high = reduce(lambda no1,no2: no1 if no1>no2 else no2,lst)
print("with highest : ",high)

# to find smallest number from the list
# low = min(lst)

low = reduce(lambda num1,num2: num1 if num1<num2 else num2,lst)
print("with lowest : ",low)




