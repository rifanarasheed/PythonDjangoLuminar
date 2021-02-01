# to print two list : oddlst, evenlst
# print two list
# find their sum
lst = [10,11,12,13,14,15,16,17]
evenlst = list()
oddlst = list()
for num in lst:
    if num%2==0:
        evenlst.append(num)
    else:
        oddlst.append(num)
print(oddlst)
print(evenlst)
print("odd sum :",sum(oddlst))
print("even sum :",sum(evenlst))

