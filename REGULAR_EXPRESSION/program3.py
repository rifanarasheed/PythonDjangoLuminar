#  a-k --> first character must be an alphabet between a-k
#  second must be a digit divisible by 3
#  followed by any number of character

from re import *
varname = input("enter the variable name")

rule = "[a-k][369][a-zA-Z0-9]*"

matcher = fullmatch(rule,varname)             # fullmatch() checks for full match of variable given in rule (not checking whether the pattern is present or not)
if matcher == None:
    print("invalid variable")
else:
    print("valid variable")