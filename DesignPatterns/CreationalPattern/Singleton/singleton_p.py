####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

''' 
    Creating the one instance for class is called singleton pattern
'''

class MetaClass(type):
    _single_instance = {} 
    
    def __call__(cls, *args, **kwds):
        """ create single instance """
        if cls not in cls._single_instance:
            cls._single_instance[cls] = super().__call__(*args, **kwds)
        return cls._single_instance[cls]
    
    
class Foot(metaclass=MetaClass):
    def __init__(self) -> None:
        pass
    
    
f = Foot()
print(f)

f1 = Foot()
print(f1)

""" 
output
>>> <__main__.Foot object at 0x7f50726a99a0>
>>> <__main__.Foot object at 0x7f50726a99a0>
"""
