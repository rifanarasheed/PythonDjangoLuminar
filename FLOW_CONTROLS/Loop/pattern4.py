#*
#**
#***
#****

for row in range(1,5):          # row = 1,2,3,4
    for col in range(1,row+1):  # col = 1, 1,2, 1,2,3, 1,2,3,4
        print("*",end=" ")      # * ** *** ****
    print()                     # next line
