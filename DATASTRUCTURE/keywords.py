# Global keyword
# to access the variable through out the program even in the methods. if any operations done, then it will reflect all throughout program
total = 70
def change():
    global total         # if this line is not given, total wiil have two values 500 and 70
    total = 50
    total*=10
    print(total)

change()
print(total)