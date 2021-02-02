# word count of each word
# hai = 2
# hello = 2

text = "hai hello hai hello"   # string object

# split is a function of string object. spliting the string character whenver spaces is seen
# and converting them into list
words = text.split(" ")        # class list

dict = {}                      # empty dictionary created to get count(key:value)

#key   value
#hai     2
#hello   2

for word in words:             # word = "hai","hello","hai","hello"
    if(word not in dict):      # if word not in dict then, its value will be 1
        dict[word] = 1
    else:
        dict[word]+=1          # if word is present in the dict, its value will be incremented
print(dict)


