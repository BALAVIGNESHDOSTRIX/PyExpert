####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

class Sensor:
    def __init__(self) -> None:
        pass
    
    def sensorOn(self):
        print("Sensor is On")
        
    def sensorOff(self):
        print("Sensor is Off")
        
class Smoke:
    def __init__(self) -> None:
        pass
    
    def smokeOn(self):
        print("Smoke is On")
        
    def smokeOff(self):
        print("Smoke is Off")
        
class Lights:
    def __init__(self) -> None:
        pass
    
    def lightOn(self):
        print("Lights On")
        
    def lightOff(self):
        print("Lights Off")
        
class Facade:
    _instance_pool = {}
    
    def __init__(self) -> None:
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._ligths = Lights()
        
    def __call__(cls, *args, **kwds):
        if cls not in cls._instance_pool:
            cls._instance_pool[cls] = super().__call__(*args, **kwds)
        return cls._instance_pool[cls]
        
        
    def Emergency(self):
        self._sensor.sensorOn()
        self._smoke.smokeOn()
        self._ligths.lightOn()
        
    def NoEmergency(self):
        self._sensor.sensorOff()
        self._smoke.smokeOff()
        self._ligths.lightOff()
        

_alert_ratio = 57

facade = Facade()

if _alert_ratio > 65:
    facade.Emergency()
else:
    facade.NoEmergency()
    