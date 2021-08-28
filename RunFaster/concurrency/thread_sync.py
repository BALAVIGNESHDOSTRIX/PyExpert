from threading import Thread
from time import sleep

ls = []

def looper(i):
    for n in range(1,i+1):
        ls.append(n)
        sleep(0.01)
        
def count(i):
    looper(i)
        
def count2(i):
    looper(i)
          
t1 = Thread(target=count, args=(5,))
t1.start()

t2 = Thread(target=count, args=(5,))
t2.start()

'''
    If using multiple threads with global variable accessing that time we should 
    aware to avoid the missing the values.
'''
print(ls)

''' 
    Thread syncing is done by join() method
'''
t1.join()
t2.join()

print(ls)

