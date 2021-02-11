from re import *

phone_number = open("phonenumber","r")

rule = "(91)?\d{10}"
for mob in phone_number:
    matcher = fullmatch(rule,mob)
    if matcher != None:
        print(mob, " is a valid number")
    else:
        print(mob," is not a valid phone number")
