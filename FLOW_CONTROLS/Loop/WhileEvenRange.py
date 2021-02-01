#program to print all even number upto the given limit
limit = int(input("enter the limit :"))   # 10
i = 1
while i<=limit:                           # 1<=10,2<=10,3<=10,4<=10,5<=10,6<=10,7<=10,8<=10,9<=10,10<=10,11<=10
    if(i%2==0):                           # 1%2==0,2%2==0,3%2==0,4%2==0,5%2==0,6%2==0,7%2==0,8%2==0,9%2==0,10%2==0
        print(i)                          # 2,4,5,6,8,10
    i+=1                                  # i = 2,3,4,5,6,7,8,9,10,11

