####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Condition 
import time, random

""" 
    Producer should not put Fruit in the queue if the queue is full

    Flow:
        - Before putting Fruit in queue, producer should check if the queue is full

        - If the queue is full, producer must wait. So call wait() on condition instance to accomplish this

        - This gives a chance to consumer to run. Consumer will consume fruit from queue which will create space in queue And then consumer should notify the producer

        - Once consumer releases the lock, producer can acquire the lock and can add Fruit to queue.
"""

fruit_queue = []

max_size_queue = 20 

condition = Condition()


class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'Guva', 'Blueberry']
        while True:
            condition.acquire()
            if len(fruit_queue) == max_size_queue:
                print("Producer waiting for Queue gets empty........")
                condition.wait()
                print("Now Fruit is consumed and got a space in queue.......")
            sing_fr = random.choice(fruits)
            fruit_queue.append(sing_fr)
            print("Producer Produced Fruit: {fr}".format(fr=sing_fr))
            condition.notify()
            condition.release()
            time.sleep(0.04)

class Consumer(Thread):
    def run(self):
        while True:
            condition.acquire()
            if not fruit_queue:
                print("Consumer waiting for consuming the Fruit.........")
                condition.wait()
            frt = fruit_queue.pop(0)
            print("Consumer Consumed Fruit: {fr}".format(fr=frt))
            condition.notify()
            condition.release()
            time.sleep(0.5)

Producer().start()
Consumer().start()