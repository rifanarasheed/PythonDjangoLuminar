from re import *

reg_number = input("enter the registration number : ")

# rule = "kl[0-9][0-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]*"
# rule = "kl[0-9]{2}[a-zA-Z]{2}[0-9]{4}"
rule = "kl[0-9]{2}[a-zA-Z]{2}\d{4}"


matcher = fullmatch(rule,reg_number)

if matcher == None:
    print("invalid registration number")
else:
    print("valid registration number")
