####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

''' 
    Meta Class is used for defining class rules 
    Example:
        - Giving the class rules and restrict the object creations
'''

class MetaClass(type):
    ''' 
        To restrict the class for creating more than 2 instance
    '''
    _instance_pool = {}
    _instance = 0
    
    def __call__(cls, *args, **kwds):
        if cls._instance < 2:
            cls._instance_pool[cls] = super().__call__(*args, **kwds)
            cls._instance += 1
            return cls._instance_pool[cls]
        return None
        
class A(metaclass=MetaClass):
    
    def __init__(self) -> None:
        pass
    
    def methodA(self):
        pass 
    

a = A()
print(a)

a2 = A()
print(a2)

a3 = A()
print(a3)


""" 
output:
>>> <__main__.A object at 0x7ff672bc3b50>
>>> <__main__.A object at 0x7ff672bc39a0>
>>> None
"""