lst = [[10,20],[21,22],[51,52],[53,54,55,56]]
numlist= [] # empty list to append lst together
for sublist in lst:   # [10,20],[21,22],[51,52],[53,54,55,56]
    for num in sublist:  # 10,20,21,22,51,52,53,54,55,56
        numlist.append((num))
print(numlist)