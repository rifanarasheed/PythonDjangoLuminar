from re import *

phone = open("phonenumber","r")

rule = "(\+)?(91)?\d{10}"

for mob in phone:
    phone_number = mob.rstrip("\n")
    if fullmatch(rule,phone_number):
        print(phone_number,"is a valid number")
    else:
        print(phone_number,"is not a valid phone number")
