# Logical Operator (&,|,^)

# Rule of AND (&):
# if any one of the input is false, then output will be false
print(True&False)
print(True&False)
print(True&True&False)
print(True&True)

# Rule of OR (|) :
# if any one of the input is True, then the output will be True
print(True|False)
print(True|True)
print(False|False)

# Rule of NOT(^) :
# if both input are same bit, then output will be False
# if both input are different bit, then output will be True
print(True ^ True)
print(True ^ False)
print(False ^ False)

print(2 & 4)
#2 -> 0010
#4 -> 0100
#=========
#     0000

print(2 | 4)
#2 -> 0010
#4 -> 0100
#=========
#     0110

print(2 ^ 4)
#2 -> 0010
#4 -> 0100
#=========
#     0110
