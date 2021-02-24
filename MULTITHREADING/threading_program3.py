import threading
import time

def display():
    for i in range(1,10):
        time.sleep(5)
        print("child thread executing")
    print(threading.currentThread().getName())

t = threading.Thread(target=display)
t.start()

for i in range(1,10):
    time.sleep(5)
    print("parent thread executing")
print(threading.currentThread().getName())
