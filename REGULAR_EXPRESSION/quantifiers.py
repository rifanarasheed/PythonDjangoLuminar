# to check quantity of pattern matching

from re import *

# pattern = "a"                          # checks in which position this pattern is present
# pattern = "a+"                         # checks in which position any number a's is present ,ie, single a or consecutive a's are present in the string, excluding any other charcter
#pattern = "a*"                           # checks in which position any number a's is present ,ie, single a or consecutive a's are present in the string, including position of other character
# pattern = "a?"                         # checks for the match in which position any number of a is present, ie, individually, not by group as well as positions of zero number of a
#pattern = "a{2}"                       # check for two times of 'a' together
pattern = "a{2,4}"                      # check for all 'a' that matches where minimum number of 'a' as group should be 2 to 4 (not below or above)

matcher = finditer(pattern,"aaaaaaababaaabbaabbba")

for match in matcher:
    print(match.start(),match.group())
