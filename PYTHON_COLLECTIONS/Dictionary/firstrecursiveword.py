# find first recursive character
# if we are using loop, it takes lot of iteration which will be time consuming
# by dictionary, we can use hashing technique
# we cant split the character here as we didnt have space or any other character
pattern = "ABAABBAC"

dict = {}                # empty dictionary

# key   value
#  A       1
#  B       1

for ch in pattern:       # ch = A,B,A
    if ch not in dict:   # ch = [A not in dict, then A = 1], [B not in dict, then B = 1],[A not in dict--> condition false]
        dict[ch] = 1
    else:
        print(ch,"is the first recursive character")  # after getting the first recursive character, need to come out of the loop
        break



