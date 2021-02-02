# file operation are of three operations :
# read
# write
# append

# READ
# step 1 : create reference
# f = open("filename","r")    r -> read

f = open("demo","r")

# print all the lines from file demo
#for lines in f:
#    print(lines)

# now we need to store each lines of demo in list
word = []                   # empty list
for lines in f:
    word.append(lines.rstrip("\n").split(" "))    # to remove \n because after every new line \n is printed in list
print(word)

# now combining all the nexted list into one -> flattening
mywords = []
for lst in word:               # lst = each inner lists
    for wrd in lst:            # wrd = each character of inner lists
        mywords.append(wrd)
print(mywords)

