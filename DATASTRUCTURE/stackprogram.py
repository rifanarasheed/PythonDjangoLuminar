# ALgorithm
# Procedure stack(top,element)
# case 1 :
#     push(element)
#     if top>=size:
#         stack full
#     else:
#         stack[top]=element
#         top+=1
# case 2 :
#     if top<=0:
#         stack empty
#     else:
#         top-=1
# case 3 :
#     for 0 to top:
#          print items

# top is the variable used for insertion and deletion
# top should be globally accessed in every method, as top's index location is important


size = int(input("enter size of stack"))                           # stack size
stack = []                                                         # empty list created to store items
top = 0                                                            # top = 0, if top = -1,problem during deletion as top will be one size up

def push():
    item = int(input("enter the element to be inserted"))
    global top
    if (top<size):
        stack.insert(top,item)
        top+=1
    else:
        print("stack overflow")

def pop():
    global top
    top-=1
    if top<0:
        print("stack is empty")
    else:
        print(stack[top],"popped out")

def display():
    for i in range(0,top):
        print(stack[i])

n=1                                                                     # for iteration
while n!=0:
    option = int(input("Enter your choice 1)Push 2)Pop 3)Display"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    n=int(input("Do you want to continue? 0) Exit  1) continue"))     # if n = 0, exit from loop.
