pattern = "ABAABBEEACEEEE"

dict = {}                # empty dictionary

for ch in pattern:       # ch = A,B,A
    if ch not in dict:   # ch = [A not in dict, then A = 1], [B not in dict, then B = 1],[A not in dict--> condition false]
        dict[ch] = 1
    else:
        dict[ch]+=1

# iterating dictionary to get keys and values
for key,value in dict.items():
    print(key,",",value)

# now to get highest value to get frequent character we need to sort value, not key
# if we directly sort dict,then key will be sorted not values.
# so to get values sorted, we use dictionary function dict.get()
print(dict)
print(dict.get("E"))         # prints values of the key "E"

dictsort = sorted(dict)      # keys will be sorted in ascending order
print(dictsort)

# as we dont need to get specific value, we wont be needing to put () after get
result = sorted(dict,key=dict.get,reverse=True)     #now values will sorted in descending order as reverse=true is given
print(result)
print(result[0])


