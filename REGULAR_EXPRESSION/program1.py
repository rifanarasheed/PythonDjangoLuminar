# regular expression --> used for pattern matching
# regular expression is present in re module

# program to print how many times matching pattern occur

from re import *                        # importing all functionalities from module re

pattern = "ab"

matcher = finditer(pattern,"abababbbbbaaaaababab")     # finditer() is used to search or find how many times pattern "ab" is present inside the string given inside the method
#                           0123456789
# finditer() returns iterable object
# so matcher is a iterator which name is given by user and to matcher finditer() result is passed as object
# looping matcher
count = 0                                              # to get of count of pattern "ab"
for match in matcher:
    print(match.start()) # position : 0,2,4,14,16,18   # start() shows in which position match has occured(pattern start position)
    print(match.group()) # group    :ab,ab,ab,ab,ab,ab # group() shows with which group object it is a match ,ie, pattern
    count+=1             # count    :1,2,3,4,5,6
print(count)
