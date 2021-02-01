lst = [10,11,12,13,14,15,16]
for num in lst:  # each elements of list lst will be assigned to num for each iteration.
    print(num)

# print even number only
for num in lst:
    if(num%2==0):
        print(num)

# to print total number of lst
sum = 0
for num in lst:
    sum+=num
print("sum:",sum)