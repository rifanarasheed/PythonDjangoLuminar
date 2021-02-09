from re import *

pattern = "[ab]"                  # in square bracket indicate in which position either a or b matches in the string
# pattern = "[a-z]"               # check for only lowercase a to z that matches
# pattern = "[A-Z]"               # check for only uppercase A to z that matches
# pattern = "[a-zA-Z]"            # check for only lowercase and uppercases of a to z A to Z that matches
# pattern = "[0-9]"               # check for digit from 0 to 9 that matches
# pattern = "[^0-9]"              # capsign ^ indicates except 0 to 9, all character matches
# pattern = "[a-zA-Z0-9]"         # check for only lowercase,uppercase letter as well as 0 to 9 digits that matches
# pattern = "[^a-zA-Z0-9]"        # check for character except lowercase,uppercase letter as well as 0 to 9 digits that matches

# there are some predefined characters which can used instead of above
# pattern = "\s"                 # check for space
# pattern = "\d"                 # check for all digits that matches --> "[0-9]"
# pattern = "\D"                 # all matches except digits --> "[^0-9]"
# pattern = "\w"                 # check for all(letter,digits) except special characters --> "[a-zA-Z0-9]"
# pattern = "\W"                 # check for all special characters except letter and digits --> "[^a-zA-Z0-9]"

          # find position where pattern matches
matcher = finditer(pattern,"abcdh _sk76")
for match in matcher:
    print(match.start(),match.group())