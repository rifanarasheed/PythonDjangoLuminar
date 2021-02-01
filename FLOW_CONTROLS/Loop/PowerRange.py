# when calculating the power, its result should be between lowerlimit and upperlimit
# printing i , not result

num = int(input("enter the power to multiply :"))        # 2                # 3
lower = int(input("enter the lowerlimit :"))             # 3                # 2
upper = int(input("enter the upperlimit :"))             # 30               # 28
for i in range(1,upper+1):                               # i in range(1,31) = 1,2,3,4,5,6  # i = 1,2,3,4
    if i**num in range(lower,upper):                     # 1*1=1-->below lowerlimit,2*2=4,3*3=9,4*4=16,5*5=25,6*6=36--> above upper limit
                                                         # 1*1*1=1, 2*2*2=8, 3*3*3=27, 4*4*4=48
        print(i)                                         # prints i where result comes in between lowerlimit and upperlimit

#or

# assigning result into variable and check whether the result comes in between lowerlimit and upperlimit, if yes, print i
for i in range(1,upper+1):
    res = i**num
    if(res>=lower)&(res<=upper):
        print(i)
