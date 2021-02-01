# how to create empty list
# lst = []
lst =list() # creating an empty list
# we cant update any element to an empty list, for that we use append() method
# lst.append = 50
# lst.append = 60
# print(lst)   [50,60] will be printed, from this we can update.

# to print 1 to 50
for i in range(1,51):
    lst.append(i)
print(lst)

# to get minimum and maximum number in lst
maxi = max(lst)
mini = min(lst)
print(maxi)
print(mini)