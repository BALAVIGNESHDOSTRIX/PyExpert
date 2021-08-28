''' 
    Threads run between like context switch on the cpu core.
    
    Scenario:
        - we have single core (A1) that supports single thread 
        - 1200 Threads Running on the core (A1) within specific interval of time
        
        constraint:
            - one core handle one thread per time only
        
        Simulation Explanation:
            - So that 1200 run specific interval on the same core 
            example:
                - If one core run on the specific time remaining thread in the wait state.
            
'''

from threading import Thread
from time import sleep

def count(i):
    for x in range(1, i+1):
        print(x)
        sleep(0.01)
        
for _ in range(2):
    t = Thread(target=count, args=(10,))
    t.start()