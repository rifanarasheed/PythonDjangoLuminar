# without extending thread class we can create thread by creating an object of thread class of threading module
# starting it.

from threading import *
import time

class MyClass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("child thread")

obj = MyClass()
t = Thread(target=obj.job)                      # if we give obj.job(), this will work normally like a method without creating thread,
t.start()

for i in range(10):
    print("main thread class")
