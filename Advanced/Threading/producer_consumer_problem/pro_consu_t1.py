####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Lock
import time, random


''' 
    The producer's job is to generate a piece of data, put it into the buffer and start again.
    At the same time, the consumer is consuming the data (i.e., removing it from the buffer) one piece at a time
'''

fruit_queue = []
lock = Lock()

class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'Guva', 'Blueberry']
        while True:
            lock.acquire()
            sing_fr = random.choice(fruits)
            fruit_queue.append(sing_fr)
            print("Producer Produced Fruit: {fr}".format(fr=sing_fr))
            lock.release()
            time.sleep(0.01)

class Consumer(Thread):
    def run(self):
        while True:
            lock.acquire()
            sing_fr = fruit_queue.pop(0)
            print("Consumer Consumed Fruit: {fr} ".format(fr=sing_fr))
            lock.release()
            time.sleep(0.01)


Producer().start()
Consumer().start()


""" 
    Note:
        1. Producer keeps on adding to the queue and consumer keeps on removing from the queue.
        
        2. Since queue is a shared variable, we keep it inside lock to avoid race condition.
        
        3. At some point, consumer has consumed everything and producer is still sleeping. 
        Consumer tries to consume more but since queue is empty, an IndexError is raised

    Result:
        This is a wrong implementation.
"""
