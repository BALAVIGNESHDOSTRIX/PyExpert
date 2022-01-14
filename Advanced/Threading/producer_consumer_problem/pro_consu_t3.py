####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Condition
import time, random

""" 
    Producer should not add a Fruit to the basket if the basket is full

    Flow:
        - Before putting Fruit to the basket, producer should check if the basket is full

        - If the queue is full, producer must wait. So call wait() on condition instance to accomplish this

        - This gives a chance to consumer consume the fruit. Consumer will consume fruit from basket which will 
        create space in basket And then consumer should notify the producer 

        - Once consumer releases the lock, producer can acquire the lock and can add Fruit to basket.
"""

fruit_basket = []

max_size_basket = 20

condition = Condition()


class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'PineApple', 'Blueberry']
        while True:
            condition.acquire()
            if len(fruit_basket) == max_size_basket:
                print("Producer waiting for Queue gets empty........")
                condition.wait()
                print("Now Fruit is consumed and got a space in queue.......")
            produced_fruit = random.choice(fruits)
            fruit_basket.append(produced_fruit)
            print("Producer Produced Fruit: {fr}".format(fr=produced_fruit))
            condition.notify()
            condition.release()
            time.sleep(0.04)


class Consumer(Thread):
    def run(self):
        while True:
            condition.acquire()
            if not fruit_basket:
                print("Consumer waiting for consuming the Fruit.........")
                condition.wait()
            consumed_fruit = fruit_basket.pop(0)
            print("Consumer Consumed Fruit: {fr}".format(fr=consumed_fruit))
            condition.notify()
            condition.release()
            time.sleep(0.5)


Producer().start()
Consumer().start()
