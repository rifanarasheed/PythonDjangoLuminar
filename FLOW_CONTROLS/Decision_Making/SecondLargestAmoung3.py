# Read three numbers
# find largest number and second largest number
# sort them in order

num1 = int(input("enter the number1 :"))
num2 = int(input("enter the number2 :"))
num3 = int(input("enter the number3 :"))
if((num1>num2)&(num1>num3)):                    # if num1 is largest
    print("num1 is largest")
    if(num2>num3):                              # possible second largest num2 and num3
        print("num2 is second largest")
        print("sorted :",num1,num2,num3)
    elif(num3>num2):
        print("num3 is second largest")
        print("sorted :",num1,num3,num2)
    elif(num2==num3):
        print("num2 and num3 are both second largest")
elif((num2>num1)&(num2>num3)):                  # if num2 is largest
    print("num2 is largest")
    if(num1>num3):                              # possible second largest num1 and num3 or both
        print("num1 is second largest")
        print("sorted :", num2, num1, num3)
    elif(num3>num1):
        print("num3 is second largest")
        print("sorted :", num2, num3, num1)
    elif(num1==num3):
        print("num1 and num3 are both second largest")
elif((num3>num1)&(num3>num2)):                  # if num3 is largest
    print("num3 is largest")
    if(num1>num2):                              # possible second largest num1 and num2 or both
        print("num1 is second largest")
        print("sorted :", num3, num1, num2)
    elif(num2>num1):
        print("num2 is second largest")
        print("sorted :", num3, num2, num1)
    elif(num1==num2):
        print("num1 and num2 are both second largest")
elif((num1==num2)&(num1==num3)):      # or else:
    print("numbers are equal")