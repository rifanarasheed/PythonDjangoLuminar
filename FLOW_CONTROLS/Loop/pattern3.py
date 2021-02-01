#1
#22
#333
#4444
for row in range(1,5):          # row = 1,2,3,4
    for col in range(1,row+1):  # col = [1,2],
        print(row,end="")       # row = 1, 2,2, 3,3,3, 4,4,4,4
    print()                     # next line

