# exception -->abnormal code(situation) termination (similar like error)
# exception handling --> how to handle the exception

# exception handling keywords:
# try --> block of doubtful code in try block,that is, codes that we feel exception may arise
# except --> block of codes how to handle the exception when it is arisen
# finally --> block of codes that has to execute mandatory even if exception occur or not(cleanup processing code)

# ex: syntax error, type error,value error,opening a file not available.

# if exception is encountered , then there will abnormal program termination and rest of the code wont be executed.
# so to avoid that we put codes which exceptions are possible in try block.
# and when these exception occur, how to handle them are given in the exception. mainly gives what is the error or whatever message we want to print

# exception is the class which handles the exception
# when printing e.args --> this will identify exact kind of error
# e is the allies which can be used as we wish, any word or letter is possible.

# either try or exception will be executed, not both together
# ie, if exception occur in try block, it will stop execution in try block and jump into except block to print error.
# so rest of the block of code in try wont be executed.

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
try:
    res = num1/num2                          # exception may occur if num2 = 0
    print("res :",res)
except Exception as e:                       # class exception with allies e to get exact error
    # print("exception has occured")
    print(e.args)                            # we need to code same way to get exact error.
print("i have one database transaction")     # will print even though exception occur
print("i have file operation")               # will print even though exception occur