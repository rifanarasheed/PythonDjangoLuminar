lst = [10,20,30]
pos = int(input("enter the position you want to print"))
try:
    print(lst[pos])                     # if the pos given is greater than length of list, then exception may occur
except Exception as e:
    print(e.args)
    # print("out of range")


lst1 = [12,35,46,78]
pos = int(input("enter the position you want to print"))
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
try:
    res = num1/num2                  # here if we give num2 = 0, exception will arise and print except block with exact error and rest of code wont be executed in try block
    print(res)
    print(lst1[pos])                 # if this code arise exception, then executing jumps into except and print error while printing res
except Exception as e:
    print(e.args)

# if we want to give exception separatly for each exception arising code, we can do that too
# so that rest of the code wont be terminated even if exception occur for a single code
# so for that each try and its corresponding except block should be given