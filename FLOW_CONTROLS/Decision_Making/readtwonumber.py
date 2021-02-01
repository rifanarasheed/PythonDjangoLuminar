# read two number
# print true if sum of two number gives 100 or any one number is 100
# else print false

num1 = int(input("enter the number1 :"))
num2 = int(input("enter the number2 :"))
sum = num1 + num2
if((sum==100)|(num1==100)|(num2==100)):
    print("True")
else:
    print("False")