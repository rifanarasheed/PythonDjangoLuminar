read = open("demo","r")       # to read file

dict = {}                     # creating an empty dictionary for counting words

for line in read:             # iterating each line
    words = line.rstrip("\n").split(" ")
    for wrd in words:         # iterating each word of each line
        if(wrd not in dict):
            dict[wrd] = 1
        else:
            dict[wrd]+=1

# to print key and values present in the dictionary
for key,value in dict.items():
    print(key,value)


