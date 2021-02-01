lst = [10,3,6,8,29,18]
flag = 0

# element =29
# step 1 : sort this list
#        : [3,6,8,10,18,29]
#           0 1 2 3 4 5 6
#           lower           upper
# step 2 :calculate mid point of list
#        :(lower+upper)//2 = 0+6//2 = 3
# step 3 : if element>lst[mid]
#          if condition true, then, lower = mid+1
# step 4 : if element<lst[mid]
# #        if condition true, then, upper = mid-1
# step 4 : if element>lst[mid]
# step 5 : if element<lst[mid]
# step 6 : if element == lower,upper,lst[mid]

# sorting list
lst.sort()

# assigning lower and upper limit
low = 0
upp = len(lst)-1
element = int(input("enter the element for search"))
while(low<upp):
    mid = (low+upp)//2
    if(element>lst[mid]):
        low = mid+1
    elif(element<lst[mid]):
        upp = mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("element not found")
else :
    print("element found")