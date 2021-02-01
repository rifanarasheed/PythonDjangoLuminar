lst = [2,5,6,7]
# 20-2=18
# 20-5=15
# 20-6=14
# 20-7=13
out=list()  # empty list
total=sum(lst)  # total =20
for num in lst: # 5
    out.append((total-num))
print(out)
    