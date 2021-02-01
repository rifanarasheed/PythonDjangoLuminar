lst = [1,4,2,5]

# i =    0 1 2 3   --> index number
# lst = [1,4,2,5]
# j =    1 2 3 4   --> index number

num = int(input("enter the number to find pairs")) # 7
for i in range(0,len(lst)):        # i = 0
    for j in range(i+1,len(lst)):  # j = i+1=1,2,3
        if(lst[i]+lst[j]==num):    # 1+4==7 ->false then j increment, 1+2==7 ->false then j increment
            print(lst[i],lst[j])