import threading
import time
import random

buffer = []
condition = threading.Condition()
MAX = 100


def Abuela():
    
    with condition: 
        while len(buffer) >= MAX: 
                condition.wait()
        if not len(buffer) >= MAX:
            buffer.append(10)
            print("add 10 galletas") 
            condition.notify() # alertar a consumidor 
        time.sleep(random.random())

def Nieto():
    pass






p = threading.Thread(target=Abuela)
c = threading.Thread(target=Nieto, daemon=True)

p.start()
c.start()
p.join()

































