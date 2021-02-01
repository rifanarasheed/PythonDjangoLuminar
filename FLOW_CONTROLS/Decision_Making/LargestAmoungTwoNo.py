# To print largest Amoung two Numbers
num1 = int(input("enter the num1:"))
num2 = int(input("enter the num2:"))
if(num1>num2):
    print("num1 is largest")
elif(num2>num1):
    print("num2 is largest")
elif(num1==num2):             # or else:
    print("Both are equal")