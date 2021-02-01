# Read three numbers
# find largest number

num1 = int(input("enter the number1 :"))
num2 = int(input("enter the number2 :"))
num3 = int(input("enter the number3 :"))
if((num1>num2)&(num1>num3)):
    print("num1 is largest")
elif((num2>num1)&(num2>num3)):
    print("num2 is largest")
elif((num3>num1)&(num3>num2)):
    print("num3 is largest")
elif((num1==num2)&(num1==num3)):      # or else:
    print("numbers are equal")