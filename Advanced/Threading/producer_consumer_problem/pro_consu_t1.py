####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Lock
import time, random

""" 
    Note:
        1. Producer keeps to adding the fruit to the basket and consumer keeps to consuming(removing) the fruit from the basket.

        2. Since basket is a shared variable, so we keep it inside lock to avoid race condition.

        3. At some point, consumer has consumed everything and producer is still sleeping. 
        Consumer tries to consume more but since queue is empty, an IndexError is raised

    Result:
        This is a wrong implementation.
"""

''' 
    The producer's job is to generate a piece of data, put it into the buffer and start again.
    At the same time, the consumer is consuming the data (i.e., removing it from the buffer) one piece at a time
'''

fruit_basket = []
lock = Lock()


class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Blueberry']
        while True:
            lock.acquire()
            produced_fruit = random.choice(fruits)
            fruit_basket.append(produced_fruit)
            print("Producer Produced Fruit: {fr}".format(fr=produced_fruit))
            lock.release()
            time.sleep(0.01)


class Consumer(Thread):
    def run(self):
        while True:
            lock.acquire()
            consumed_fruit = fruit_basket.pop(0)
            print("Consumer Consumed Fruit: {fr} ".format(fr=consumed_fruit))
            lock.release()
            time.sleep(0.01)


Producer().start()
Consumer().start()