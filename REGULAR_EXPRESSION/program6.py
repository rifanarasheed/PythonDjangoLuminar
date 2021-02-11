from re import *

email_id = input("enter the email id : ")

rule = "[a-zA-Z.]*[/d]*@gmail.com"

matcher = fullmatch(rule,email_id)

if matcher == None:
    print("invalid email id")
else:
    print("valid email id")