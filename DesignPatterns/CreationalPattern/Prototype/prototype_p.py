####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "10/05/2021"               #
####################################

class BMIPrototype:
    
    def __init__(self):
        self._weight = 0
        self._height = 0

    def calBMI(self):
        return int(self._weight / (self._height * 0.01)**2)

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class ObjectRegistry:
    def __init__(self):
        self._objects = {}

    def register(self,name,obj):
        self._objects[name] = obj

    def unregister(self,name):
        del self._objects[name]

    def getObjects(self):
        return self._objects.items()

object_reg = ObjectRegistry()
bmi_proto = BMIPrototype()


obj1 = bmi_proto.clone(_weight=45, _height=174)
obj2 = bmi_proto.clone(_weight=55, _height=170)
obj3 = bmi_proto.clone(_weight=55, _height=170)

object_reg.register('bala', obj1)
object_reg.register('arul', obj2)
object_reg.register('pradeep', obj3)


for person,obj in object_reg.getObjects():
    print(person, "=======> BMI ========>", obj.calBMI(),"======> Object ID =========>" , id(obj))  