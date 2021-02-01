#program to print all even number with lower limit as well as upper limit

lowerlimit = int(input("enter the lowerlimit"))    # 3
upperlimit = int(input("enter the upperlimit"))    # 10
while lowerlimit<=upperlimit:                      # 3<=10,4<=10,5<=10,6<=10,7<=10,8<=10,9<=10,10<=10,11<=10
    if(lowerlimit % 2 == 0):                       # 3%2==0,4%2==0,5%2==0,6%2==0,7%2==0,8%2==0,9%2==0,10%2==0
        print(lowerlimit)                          # 4,6,8,10
    lowerlimit+=1                                  # 4,5,6,7,8,9,10,11