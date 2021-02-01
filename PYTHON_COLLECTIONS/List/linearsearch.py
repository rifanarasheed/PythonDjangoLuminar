

lst = [10,11,12,13,14,15]
element = int(input("enter the number to be found : "))
flag = 0
pos = 1
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    pos+=1
if flag==0:
    print("element not found")
else:
    print("element found at ",pos)