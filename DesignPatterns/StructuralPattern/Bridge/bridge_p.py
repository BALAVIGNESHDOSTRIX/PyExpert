####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from abc import ABC, abstractmethod

''' 
    Problem:
        - For example, imagine we have a class structure including medieval buildings. We have a wall, tower, stable, mill, house, armory, etc. 
    We now wanted to differentiate them based on which materials they're made out of. We could derive every class and make straw_wall, log_wall, 
    cobblestone_wall, limestone_watchtower, etc...
    Furthermore, a tower could be extended into a watchtower, lighthouse, and castle_tower

    Solution:
        - To avoid this, we'll take out the fundamental information and make it a common ground upon which we'll build variations. In our case, 
    we'll separate a class hierarchy for a Building and Material.
    We'll want to have a bridge between all Building subclasses and all Material subclasses so that we can generate variations of them, without having to 
    define them as separate classes
'''

# MaterialInterface & material subclass
class MaterialInterface(ABC):

    @abstractmethod
    def __str__(self):
        pass

class LimesStone(MaterialInterface):

    def __str__(self):
        return "limestone"


class CobbleStone(MaterialInterface):

    def __str__(self):
        return "cobblestone"


class Wood(MaterialInterface):

    def __str__(self):
        return "Wood"

class Concerete(MaterialInterface):

    def __str__(self):
        return "concerete"


# BuildingInterface & building subclass
class BuildingInterface(ABC):

    @abstractmethod
    def print_name(self):
        pass 

class Mill(BuildingInterface):
    def __init__(self, building_name, material_name):
        self.bulid_name = building_name
        self.material = material_name

    def print_name(self):
        print("{material} Mill - {building}".format(material=self.material, building=self.bulid_name))


class Tower(BuildingInterface):
    def __init__(self, building_name, material_name):
        self.bulid_name = building_name
        self.material = material_name

    def print_name(self):
        print("{material} Tower - {building}".format(material=self.material, building=self.bulid_name))

class House(BuildingInterface):
    def __init__(self, building_name, material_name):
        self.bulid_name = building_name
        self.material = material_name

    def print_name(self):
        print("{material} House - {building}".format(material=self.material, building=self.bulid_name))



wood = Wood()
woodtower = Tower("Sentry hob", wood)
woodtower.print_name()