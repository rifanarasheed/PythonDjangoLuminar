num1 = int(input("enter num1"))  # if int is not, string object will be created
num2 = int(input("enter num2"))
print("BEFORE SWAPPING")
print("NUM1 :",num1)
print("NUM2 :",num2)
temp = num1     # temp = 10
num1 = num2     # num1 = 20
num2 = temp     # num2 = 10
print("AFTER SWAPPING")
print("NUM1 :",num1)
print("NUM2 :",num2)

# ANOTHER METHOD WITHOUT TEMP VARIABLE
# num1 = num1 + num2       ->    num1 = 10+20 = 30
# num2 = num1 - num2       ->    num2 = 30-20 = 10
# num1 = num1 - num2       ->    num1 = 30-10 = 20

# "hello" + "hello"  -> "hellohello"
# "hello" + 24       ->  type error because we cannot concatenate different datatype