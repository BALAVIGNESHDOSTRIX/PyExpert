####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from threading import Thread, Condition
import random, time

"""When there is nothing in the basket, a consumer should have to stop consuming and wait, and once the producer 
produces fruit and add it to the basket there should be a way for it to notify the consumer telling it has added 
something to the basket. So, the consumer can again consume from the basket and therefore IndexError will never be 
raised. 

    - Condition object allows one or more threads to wait until notified by another thread
    - Condition is always associated with a lock
    - A condition has acquire() and release() methods that call the corresponding methods of the associated lock
"""

""" 
    Note:
        - For consumer, we check if the basket is empty before consuming

        - If yes then call wait() from condition class

        - wait() blocks the consumer for consume the fruit and also releases the lock associated with the condition. 
          This lock was held by consumer, so basically consumer will loss a lock

        - Producer can acquire the lock because lock was released by consumer

        - Producer produce to add a fruit to basket and calls notify() from condition class

        - Once notify() call is made on condition, consumer wakes up. But waking up does not mean it starts executing

        - notify() does not release the lock. Even after notify(), lock is still held by producer

        - Producer explicitly releases the lock by using condition.release()

        - And consumer starts consuming again. Now it will find fruit in basket for consuming so no IndexError will be raised
"""

fruit_basket = []

condition = Condition()


class Producer(Thread):
    def run(self):
        fruits = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Blueberry']
        while True:
            condition.acquire()
            produced_fruit = random.choice(fruits)
            fruit_basket.append(produced_fruit)
            print("Producer Produced Fruit: {fr}".format(fr=produced_fruit))
            condition.notify()
            condition.release()
            time.sleep(0.9)


class Consumer(Thread):
    def run(self):
        while True:
            condition.acquire()
            if not fruit_basket:
                print("Consumer waiting for consuming the Fruit.........")
                condition.wait()
            consumed_fruit = fruit_basket.pop(0)
            print("Consumer Consumed Fruit: {fr}".format(fr=consumed_fruit))
            condition.release()
            time.sleep(0.1)


Producer().start()
Consumer().start()
