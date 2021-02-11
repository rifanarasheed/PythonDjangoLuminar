from re import *

reg_no = open("vehicle","r")

rule = "kl[0-9]{2}[a-zA-Z]{2}\d{4}"

for reg in reg_no:
    if (fullmatch(rule,str(reg))):
        print(reg," is valid registration number")
    else:
        print(reg," is not a valid registration number")