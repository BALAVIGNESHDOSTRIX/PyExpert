####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from library import VehicleInterface, Bus 


''' 
    Adapter Pattern Design
        The Adapter Pattern applies the same idea to object-oriented programming by introducing an additional adapter class between an interface 
    and an existing class. The adapter class implements the expected interface and keeps a reference to an object of the class you want to 
    reuse.
    
    Types of Adapter:
        1. Object Adapter
        2. Class Adapter

    Pros & Cons
        1. Use Object Adapter becuase it is loosle coupled
        2. Don't use Class Adapter because it is complex and inheritence overhead

    Problem:
        - From library import Bus class only having the engineModel method that is not having the wheels method but we
    don't touch to modifiy or implement the new functionality in library file so for that we will create the adapter to 
    get the solution for that.
'''

class BusAdapter(VehicleInterface):
    def __init__(self, bus_instance):
        self.bus = bus_instance

    def wheels(self):
        print("4 Wheels Bus type..........")
        return super().wheels()

    
bus = Bus()
busadapter = BusAdapter(bus)
busadapter.wheels()
bus.engineModel()
        