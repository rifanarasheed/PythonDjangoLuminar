studentlist = ["raj","riya","rahul","rahul","john","rohit"]
faillist = ["raj","riya"]

# converting into set
studentset = set(studentlist)
failset = set(faillist)
passset = set()


# to get students who got passed
passset = studentset.difference(failset)

print("students : ",studentset)
print("passed students :",passset)
print("failed students :",failset)
