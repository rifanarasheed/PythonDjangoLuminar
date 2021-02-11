from re import *

mobile_no = input("enter the mobile number")

rule="(91)?\d{10}"                        # checks for 91 is present or not, both are valid and 10 digits mandatory

matcher = fullmatch(rule,mobile_no)

if matcher == None:
    print(":invalid mobile number")
else:
    print("valid mobile number")



