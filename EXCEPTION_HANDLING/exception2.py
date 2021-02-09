# nested try exception
# how to handle exception depends upon programmer.
# when try block execute successfully, then finally block execute.
# when all exception are executed then also finally block execute.

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
try:
    res = num1/num2                               # if num2 = 0, then its corresponding except will work
    print(res)
except:
    num2 = int(input("num2 : "))                  # to give value to num2 again
    try:
        res = num1 / num2                         # if num1 = 0,again exception arises and jump to except code
        print(res)
    except:
        num2 = int(input("num2 : "))              # it goes on...
        res = num1 / num2
        print(res)
        try:
            num2 = int(input("num2 : "))
        except Exception as e:                    # we can give this way too,ie, how to handle exception
            print(e.args)
finally:                                           # mandatory block that will execute
    print("i have one database transaction")
    print("i have file operation")

