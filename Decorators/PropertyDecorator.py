'''
        DEVELOPER NAME: M.BALAVIGNESH

        IMPLEMENTED DATE: 23/06/2019

        Scope Of Implementation:  To understanding the property decorator.
'''

class Method:
    def __init__(self, name):
        self._name = name 

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        self._name = name 

    @name.getter
    def getname(self):
        return self._name

if __name__ == "__main__":
    pp = Property("Balavignesh")
    print(pp.name)
    pp.name = "JULIUSBALA"
    print(pp.name) 
    print(pp.getname)
