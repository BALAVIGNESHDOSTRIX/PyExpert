####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

from abc import abstractmethod, ABC

class VehicleInterface(ABC):
    ''' Vehicle Interface '''
    @abstractmethod
    def wheels(self):
        pass 


class Bike(VehicleInterface):

    def engineModel(self):
        print("AST-GH Model")

    def wheels(self):
        print("2 Aloy Wheels")
        return super().wheels()


class Bus:
    def engineModel(self):
        print("HTYIO Hydra Model")
