names = ["india","pak","australia","england","south america","srilanka"]
def upper(name):
    return name.upper()

lst1 = list(map(upper,names))
print("with method : ",lst1)

# using lambda function
lst = list(map(lambda name:name.upper(),names))
print("with lambda : ",lst)

#