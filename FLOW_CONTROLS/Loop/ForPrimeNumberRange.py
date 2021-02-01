# to print prime number between lower limit and upper limit

lower = int(input("enter the lowerlimit :"))# 4
upper = int(input("enter the upperlimit :"))# 20

# first for loop --> iterating from lowerlimit to upperlimit
# second for loop --> iterating from 2 to each number coming from first for loop(same like checking whether number is prime or not

for num in range(lower,upper+1):            # num =  4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    flag = 0                                # flag = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    for i in range(2,num):                  # i = (2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(2,15),(2,16),(2,17),(2,18),(2,19),(2,20)
        if(num%i==0):                       # [4%2==0],[5%2==0,5%3==0,5%4==0],[6%2==0],[7%2==0,7%3==0,7%4==0,7%5==0,7%6==0],[8%2==0],.......................till 20%19==0
            flag=flag+1                     # flag = 1 whenver if condtion becomes true and goes break to come out of the inner loop and goes to next iteration of outer loop
            break
        else:
            flag= 0                         # flag = 0 whenver if condition becomes false and goes to next iteration of loop
    if(flag==0):                            # whenver flag becomes 0, that num will be printed.
        print(num)                          # 5,7

# first for loop has range from lower limit = 4 to upper limit = 20 ,
# in first iteration, num = 4, then flag = 0 has set.
# second for loop has range from 2 to num.
# in first iteration of second for loop -> i = 2 to 4.
# check whether 4%2==0 -> if true then flag = 1 and break statement which results in exiting from second loop.
# and checks whether flag==0, condition is false, so num will not be printed. goes to next iteration in  first loop

# next iteration, num = 5, then flag = 0 has set.
# in first iteration of second for loop -> i = 2 to 5.
# check whether 5%2==0 -> condition false, goes to else condition and flag = 0, again iterates and i = 3
# check whether 5%3==0 -> condition false, goes to else condition and flag = 0, again iterates and i = 4
# check whether 5%4==0 -> condition false, goes to else condition and flag = 0, reached the range limit of second loop
# comes out of the loop and check if condition whether flag ==0 , condition true then num is printed.
# goes to next iteration in first loop.

