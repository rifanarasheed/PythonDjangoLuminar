# number of arguments in the form of tuple in --> *args
def add(*args):                 # arguments accepted in tuple format
    return sum(args)

total = add(10,20,30)
print(total)

# if we just pass values only, it will be difficult to understand what that specific value means
# for that we use kwargs (key word arguments), same like key and value
# same like sorted() used in dictionary to get key's value
#number of arguments accepted in the form of dictionary
def print_data(**kwargs):
    print(kwargs)

print_data(name = "ajay",workplace = "kakkanad",home = "thrissur")

