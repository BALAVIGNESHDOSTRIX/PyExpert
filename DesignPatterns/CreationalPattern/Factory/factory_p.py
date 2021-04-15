####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from abc import ABC, abstractmethod
''' 
    Problem:
        - If your creating the insurance application for client for to check and 
    giving the insurance only for employed peoples. so you can created and deployed.
    client is using that after few months clients giving a new requirement for adding
    new feature for giving the insurance for unemployed person. so this situation you
    have to entirely create new class and deployed but in general scenario you don't
    know which one of the class object will call by client.
    
    Solution:
        - To overcome this situation the factory design pattern is helping a developer
    to make a standard interface for creating a different class objects.
    
        - we can create a different objects dynamically in runtime through standadard
    interface
'''

class CreditInterface(ABC):
    @abstractmethod
    def CreditRisk(self):
        pass 
    

class Employed(CreditInterface):
    def __init__(self, name, age, hrs_wrk_week) -> None:
        self._name = name
        self._age = age 
        self.hrs_week = hrs_wrk_week
        
    def CreditRisk(self):
        if self._age >= 25 and self._age <= 48 and self.hrs_week >= 38:
            return "Eligible"
        return "UnEligible"
    
    def __str__(self) -> str:
        return "{name} - age:{age} - insurance status:{ins}".format(
            name=self._name, 
            age=self._age,
            ins=self.CreditRisk()
        )
        
class UnEmployed(CreditInterface):
    def __init__(self, name, age, able=False) -> None:
        self._name = name
        self._age = age 
        self._able = able
        
    def CreditRisk(self):
        if (self._able and self._age <= 45) or (not self._able and self._age <= 36) :
            return "Eligible"
        return "UnEligible"
    
    def __str__(self) -> str:
        return "{name} - age:{age} - insurance status:{ins}".format(
            name=self._name, 
            age=self._age,
            ins=self.CreditRisk()
        )
        
class AnalyzeFactory:    
    
    @staticmethod  
    def getStatusFactory(name="",age=0,hrs_wrk=0,type_of_person="",able=False):
        return {"employed":Employed(name, age, hrs_wrk),
                "unemployed":UnEmployed(name, age, able)
                }.get(type_of_person)
        
anyzfac = AnalyzeFactory()
p1 = anyzfac.getStatusFactory(name="Jamesh",age= 30,hrs_wrk=48,type_of_person="employed")
p2 = anyzfac.getStatusFactory(name="Angelina",age=45,able=False,type_of_person="unemployed")

print(p1)
print(p2)