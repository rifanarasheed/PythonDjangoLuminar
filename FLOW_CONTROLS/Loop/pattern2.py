#1
#12
#123
#1234
for row in range(1,5):          # row = 1,2,3,4
    for col in range(1,row+1):  # col = [1,2],[1,3],[1,4],[1,5]
        print(col,end="")       # col = 1, 1,2, 1,2,3, 1,2,3,4
    print()                     # next line

