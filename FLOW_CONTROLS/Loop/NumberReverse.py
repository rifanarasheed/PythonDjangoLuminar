num = int(input("enter the number"))    # 123
res = 0
while num > 0:                          # if 123>0,12>0,1>0,0>0 -> condition false
    rev_num = num % 10                  # rev_num = 123%10=3,12%10=2,1%10=1
    res = res * 10 + rev_num            # res = 0*10+3=3,3*10+2=32,32*10+1=321
    num = num//10                       # num = 123//10=12,12//10=1,1//10=0
print(res)                              # 321

# Another Method :
# ex: num = "5"
#     num+"4"     # 54 ,not 9


#res= ""
#while num>0:
    #rev_num = num % 10
    #res = res + str(rev_num)
    #num = num // 10
#print(res)