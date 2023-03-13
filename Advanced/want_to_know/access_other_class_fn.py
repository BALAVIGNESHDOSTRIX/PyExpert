""" 
    DEVELOPER: M BALAVIGNESH
    DATE	 : 13/03/2023
    LICENSE	 : MIT
"""

class LandFactory:
    
    def __init__(self, type_of_vehicle=None, no_of_wheels=4, transmission_type='auto',
                have_to_manufacture_c=1, model_name="") -> None:
        self._type_of_vehicle = type_of_vehicle
        self._no_of_wheels = no_of_wheels
        self._transmission_type = transmission_type
        self._have_to_manufacture_c = have_to_manufacture_c
        self._model_name = model_name
        
    def vehicle_factory_info(self):
        print("Model Name: ", self._model_name) 
        print(f"Total Manufactured {self._type_of_vehicle}", self._have_to_manufacture_c)
        print(f"Transmission type: {self._transmission_type}")
        
    def vehicle_public_info(self):
        print("Model Name: ", self._model_name) 
        print(f"Total Manufactured {self._type_of_vehicle}", self._have_to_manufacture_c)
        print(f"Transmission type: {self._transmission_type}")
        print(f"No of wheels: {self._no_of_wheels}")
        
        
class AirLineFactory:
    
    def __init__(self, type_of_vehicle=None, no_of_engine=2, transmission_type='auto',
                have_to_manufacture_c=1, model_name="") -> None:
        self._type_of_vehicle = type_of_vehicle
        self._transmission_type = transmission_type
        self._have_to_manufacture_c = have_to_manufacture_c
        self._model_name = model_name
        self._no_of_engine = no_of_engine
        
    def aircraft_factory_info(self):
        """aircraft_factory_info

        This method is like a interface to access the other class method
        """
        LandFactory.vehicle_factory_info(self)
        
    def aircraft_public_info(self):
        print("Model Name: ", self._model_name) 
        print(f"Total Manufactured {self._type_of_vehicle}: {self._have_to_manufacture_c}")
        print(f"Transmission type: {self._transmission_type}")
        print(f"No of engine: {self._no_of_engine}")
        

if __name__ == "__main__":
    
    plane = AirLineFactory(
        "Fighter Jet", 2, "AIAAT", 100, "MaxGear"
    )
    
    plane.aircraft_public_info()