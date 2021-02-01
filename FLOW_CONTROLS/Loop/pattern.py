# 1234
# 5678
# 9101112

for i in range(1,13):
    if i%4!=0:                # 1%4!=0,2%4!=0,3%4!=0,4%4!=0 -> false goes to else condition,,5%4!=0,6%4!=0,7%4!=0,..,12%4!=0
        print(i,"\t",end="")  # 1,2,3,5,6,7,9,10,11,
    else:
        print(i)              # 4,8,12
        print()               # next line