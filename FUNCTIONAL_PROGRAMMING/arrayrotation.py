# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(d):                                               # determine number of rotation needed
        temp = arr[0]                                                # first element of the array is stored in variable temp
        for i in range(n - 1):                                       # shifting every element to left side by one element each(iterating till size-1 = 6)
            arr[i] = arr[i + 1]
        arr[n - 1] = temp                                            # to the last location of the array storing the temp variable value
    for i in range(n):
        print(arr[i], end=" ")


def rightRotate(arr,d,n):
    for i in range(d):
        temp = arr[n-1]
        for i in range(n-1,-1,-1,):
            arr[i]=arr[i-1]
        arr[0]= temp
    for i in range(n):
        print(arr[i], end=" ")

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7                                                            # size of array
d = int(input("enter number of rotation required: "))            # no of rotation
i=1
while i!=0:
    rotation = int(input(" 1)left rotation 2)right rotation"))
    if rotation == 1:
        leftRotate(arr,d,n)
    elif rotation == 2:
        rightRotate(arr,d,n)
