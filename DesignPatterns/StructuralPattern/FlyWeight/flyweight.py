####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

""" 
    Problem:
        - Think you are wonderful video game developer so you are creating a racing game
    for playing in this covid lockdown. now you created and enjoyed with playing. so you
    decide to give this game to your friend. now he installed that game when he playing a game
    it gets crashed many times. so he not happy for that game and told to you. after serious of 
    testing you found the issue RAM is a problem because you are game developer and having
    supercool system with high configuration but your friend not have like that.
    
    Solution:
        - creating many instance in runtime that will eat more RAM so for reducing the RAM
    and adopt to run the game on all different system we need to use the flyweight design
    pattern to overcome
    
    Concept:
        - For example we need to create 7 similer type of same value objects for 7 diffrenet works. 
    we dont create the 7 instance this will eat up your RAM for overcome to this problem we can 
    create the single instance and make that instance like a cache object and we can change
    its arribute value to use (Or) we can use that single instance for those 7 works.
"""

class BulletContext:
    def __init__(self, x, y, velocity, range, color, bull_name) -> None:
        self.x = x 
        self.y = y
        self.velocity = velocity
        self.range = range
        self.color = color
        self.name = bull_name
        
    def getBulletInfo(self):
        return "[{name} - {color} - {x} - {y} - {veloc} - {ran}]".format(
            name = self.name, color=self.color, x = self.x, 
            y = self.y, veloc = self.velocity, ran = self.range)
        
        
class BulletFactory(object):
    _bullet_instance_pool = {}
    
    def __new__(cls, x,y,velocity,rage, color, bullname, obj_modify=False):
        try:
            obj = cls._bullet_instance_pool[(x,y,velocity,rage)]
        except:
            obj = BulletContext(x,y,velocity, rage, color, bullname)
            cls._bullet_instance_pool[(x,y,velocity,rage)] = obj
        if obj_modify:
            obj.color = color
            obj.name = bullname
        return obj
    
    
bullets = [(1,1,4,5,"red","little boy"), (1,2,3,5,"green","Finshot"),
           (1,1,4,5,"blue","little girl"), (1,4,3,6,"red","sliver blade")]

for bullet in bullets:
    bult = BulletFactory(bullet[0], bullet[1], bullet[2], bullet[3], bullet[4], bullet[5], True)
    print("Object ID: ", id(bult))
    print("Bullet Info: ", bult.getBulletInfo())
    print("\n")
    
""" 
# without object value modifying (obj_modify=False)
Object ID:  140668560565008
Bullet Info:  [little boy - red - 1 - 1 - 4 - 5]


Object ID:  140668560943520
Bullet Info:  [Finshot - green - 1 - 2 - 3 - 5]


Object ID:  140668560565008
Bullet Info:  [little boy - red - 1 - 1 - 4 - 5]


Object ID:  140668560943904
Bullet Info:  [sliver blade - red - 1 - 4 - 3 - 6]
"""

""" 
# with object value modifying (obj_modify=True)
Object ID:  140385283998384
Bullet Info:  [little boy - red - 1 - 1 - 4 - 5]


Object ID:  140385283856704
Bullet Info:  [Finshot - green - 1 - 2 - 3 - 5]


Object ID:  140385283998384
Bullet Info:  [little girl - blue - 1 - 1 - 4 - 5]


Object ID:  140385283857088
Bullet Info:  [sliver blade - red - 1 - 4 - 3 - 6]
"""