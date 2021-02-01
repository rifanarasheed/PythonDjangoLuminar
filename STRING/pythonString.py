# String is a sequence of characters
# single,double quote can be used.
# triple quote """ """ can be used when we want string to be used in multiple line.

name = "luminar technolab"          # string object created

#split method
words = (name.split(" "))           # space is the condition to split in this current string
print(words)

#upper method
print(name.upper())                 # converting into uppercase

#lower method
print(name.lower())                 # converting into lowercase

name = "TTluminartechnolabTT"       # assigned new value as TTluminartechnolabTT to name object
print(name)

name = name.lstrip("TT")            #removing first charcter of a string
print(name)

name = name.rstrip("TT")            #removing last charcter of a string
print(name)