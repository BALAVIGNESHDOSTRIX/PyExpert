####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from abc import ABC, abstractmethod
''' 
    Problem:
        - Imagine you're running a delivery service, and suppliers send big boxes full of items via your company. You'll want to know the value of the items inside because you charge fees for high-valued packages. 
    Of course, this is done automatically, because having to unwrap everything is a hassle. This isn't as simple as just running a loop, because the structure of each box is irregular. 
    You can loop over the items inside, sure, but what happens if a box contains another box with items inside? How can your loop deal with that? Sure, 
    you can check for the class of each looped element, but that just introduces more complexity. The more classes you have, the more edge-cases there are, leading to an unscalable system

    Solution:
        - A good way to deal with a structure like this is having the object directly above controlling the behavior of those below it. 
    we could make every box contain a list of its contents, and make sure all boxes and items have a function - return_price(). If you call return_price() on a 
    box, it loops through its contents and adds up their prices (also calculated by calling their return_price()), and if you have an item it just returns its price
'''


class ItemInterface(ABC):

    @abstractmethod
    def return_price(self):
        pass 


class Box(ItemInterface):

    def __init__(self, boxes):
        self.boxes = boxes
        
    def return_price(self):
        price = 0
        for box in self.boxes:
            price += box.return_price()
        return price


class Mobile(ItemInterface):
    
    def __init__(self, price):
        self.cost = price

    def return_price(self):
        return float(self.cost)


class Buletooh(ItemInterface):

    def __init__(self, price):
        self.cost = price
                
    def return_price(self):
        return self.cost


class HeadPhone(ItemInterface):
    def __init__(self, price):
        self.cost = price
                
    def return_price(self):
        return self.cost


# Simulation

# phoneBox

big_box_contents = []
phone_box_contents = []
iphone = Mobile(500)
nokia = Mobile(7000)
motorola = Mobile(5000)
phone_box_contents.append(iphone)
phone_box_contents.append(motorola)
phone_box_contents.append(nokia)
phone_box = Box(phone_box_contents)

headphones = HeadPhone(5932)
bluetooth = Buletooh(9834)
big_box_contents.append(phone_box)
big_box_contents.append(headphones)
big_box_contents.append(bluetooth)

root_box = Box(big_box_contents)
print(root_box.return_price())

