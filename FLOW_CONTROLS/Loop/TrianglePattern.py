#   *
#  * *
# *   *
#*******

for row in range(1,5):                           # i = 1
    for col in range(1,8):                       # j = 1,2,3,4
        if(row==4)|(row+col==5)|(col-row==3):    # if condition true, then print *
            print("*",end="")
        else:                                    # else condition true, then give space
            print(end=" ")
    print()                                      # next line
