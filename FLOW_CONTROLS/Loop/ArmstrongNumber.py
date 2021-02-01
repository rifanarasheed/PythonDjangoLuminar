#1*1*1+2*2*2+3*3*3 = 1+8+27 = 36

num = int(input("enter the number"))  # 123
res = 0
while num > 0:                        # 123>0,12>0,1>0,0>0 -> condition false
    digit = num % 10                  # digit = 123%10=3,12%10=2,1%10=0
    res = res + digit ** 3            # res = 0+3**3(3 power)=27,27+2**3=35,35+1**3=36
    num = num // 10                   # num = 123//10=12,12//10=1,1//10=0
print(res)