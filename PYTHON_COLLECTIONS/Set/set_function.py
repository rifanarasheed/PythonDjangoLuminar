st1 = {10,20,30,40}
st2 = {30,40,50,60,70,80}

# Union : takes all the elements from set1 and set2
# 10,20,30,40,50,60,70,80
unionset = st1.union(st2)
print(unionset)

# Intersection : takes all the common elements of set1 and set2
# 30,40
insectset = st1.intersection(st2)
print(insectset)

# difference : removing elements present in set2 from set1
differset = st1.difference(st2)
print(differset)

