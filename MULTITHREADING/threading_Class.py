from threading import *

class Mythread(Thread):                          # inherting thread class from threading module
    def run(self):                               # run() is method which is present in thread class of threading mocule, we override that method
        for i in range(10):
            print("inside thread class")

obj = Mythread()
obj.start()                                      # start() creates thread and then run() method will be activated automatically. if we give run() instead of start(), normally run() method will be executed without creating thread

for i in range(10):
    print("main thread class")