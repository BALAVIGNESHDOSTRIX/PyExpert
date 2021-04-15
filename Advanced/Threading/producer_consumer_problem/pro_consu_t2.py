####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Condition
import random, time 

"""
    When there was nothing in the queue, consumer should have stopped running and waited instead of trying to consume from the queue. 
    And once producer adds something to the queue, there should be a way for it to notify the consumer telling it has added something to queue. 
    So, consumer can again consume from the queue. And thus IndexError will never be raised.

    - Condition object allows one or more threads to wait until notified by another thread
    - Condition is always associated with a lock
    - A condition has acquire() and release() methods that call the corresponding methods of the associated lock
"""

fruit_queue = []

condition = Condition()

class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'Guva', 'Blueberry']
        while True:
            condition.acquire()
            sing_fr = random.choice(fruits)
            fruit_queue.append(sing_fr)
            print("Producer Produced Fruit: {fr}".format(fr=sing_fr))
            condition.notify()
            condition.release()
            time.sleep(0.9)

class Consumer(Thread):
    def run(self):
        while True:
            condition.acquire()
            if not fruit_queue:
                print("Consumer waiting for consuming the Fruit.........")
                condition.wait()
            frt = fruit_queue.pop(0)
            print("Consumer Consumed Fruit: {fr}".format(fr=frt))
            condition.release()
            time.sleep(0.1)


Producer().start()
Consumer().start()


""" 
    Note:
        - For consumer, we check if the queue is empty before consuming
        
        - If yes then call wait() on condition instance
        
        - wait() blocks the consumer and also releases the lock associated with the condition. 
          This lock was held by consumer, so basically consumer loses hold of the lock
        
        - Producer can acquire the lock because lock was released by consumer

        - Producer puts Fruit in queue and calls notify() on the condition instance

        - Once notify() call is made on condition, consumer wakes up. But waking up doesn’t mean it starts executing

        - notify() does not release the lock. Even after notify(), lock is still held by producer

        - Producer explicitly releases the lock by using condition.release()

        - And consumer starts running again. Now it will find fruit in queue and no IndexError will be raised
"""


