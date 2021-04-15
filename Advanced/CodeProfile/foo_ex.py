####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from logger import log

class Foo(object):
    
    def __init__(self) -> None:
        pass
    
    @log()
    def methodQ(self, x,y,z):
        return x**y*z 
        
foo = Foo()
res = foo.methodQ(20,40,5)
print(res)

