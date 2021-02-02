# queue is first in - first out

size = int(input("enter the size of queue : "))
queue = []
rear = 0                                               # rear for insertion
front = 0                                              # front for deletion

def insert():
    element = int(input("enter the element : "))
    global rear
    if rear>=size:
        print("queue is full")
    else:
        queue.insert(rear,element)
        rear+=1

def delete():
    global front
    if front==rear:
        print("queue empty")
    else:
        print(queue[front]," deleted")
        front+=1

def display():
    if front == rear:
        print("Empty Queue")
    else:
        for i in range(0,rear):
            print(queue[i])

n=1
while n!=0:
    option = int(input("Enter your choice 1)Insert 2)Delete 3)Display"))
    if option==1:
        insert()
    elif option==2:
        delete()
    elif option==3:
        display()
    n=int(input("Do you want to continue? 0) Exit  1) continue"))     # if n = 0, exit from loop.


