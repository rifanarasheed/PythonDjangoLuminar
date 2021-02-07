# to print names of countries whose starting letter is "a"
names = ["india","pak","australia","england","south america","srilanka","anartica","america"]

def starta(name):
    return name[0]=="a"

acountrylst = list(filter(starta,names))
print("with method : ",acountrylst)

# using lambda function
acountry = list(filter(lambda name:name[0]=="a",names))
print("with lambda : ",acountry)
