# list flattening

lst = [[34,45],[56,89],[56,90]]

# 1.
#newlist = []
#for ls in lst:
#    for i in ls:
#        newlist.append(i)
# print(newlist)

# 2. using list comprehension
new_list = [num for ls in lst for num in ls]
print(new_list)
