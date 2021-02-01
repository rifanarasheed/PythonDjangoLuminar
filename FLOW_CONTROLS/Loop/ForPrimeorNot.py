#A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
# prime number starts from 2 because 1 is neither prime nor not prime

# to check given number is prime or not

num = int(input("enter the number"))  # 7
flag = 0                              # flag = 0
if num == 1:                          # 7 == 1 -> condition false
    print("not prime")
else:
    for i in range(2,num):            # i = 2,3,4,5,6  (i starts from 2 to num)
        print(i)
        if(num % i == 0):             # 7%2==0,7%3==0,7%4==0,7%5==0,7%6==0 -> all false conditions because 7 have no other factor except 1 and 7
            flag = flag + 1           # once if condition becomes true and flag becomes 1,
            break                     # then break statements is executed as we don't need to do further iterations as number is not prime
        else:
            flag = 0                 # flag = 0,0,0,0,0
if flag == 0:                        # condition true, prints prime
    print("prime")
else:
    print("not prime")
