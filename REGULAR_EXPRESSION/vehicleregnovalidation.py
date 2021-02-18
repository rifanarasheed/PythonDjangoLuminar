from re import *

reg = open("vehicle","r")

rule = "KL[0-9]{2}[a-zA-Z]{2}\d{4}"

for reg in reg:
    reg_no = reg.rstrip("\n")
    if (fullmatch(rule,reg_no)):
        print(reg_no," is valid registration number")
    else:
        print(reg_no," is not a valid registration number")