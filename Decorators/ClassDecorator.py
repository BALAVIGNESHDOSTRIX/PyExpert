'''
        IMPLEMENTATION DATE: 23/06/2019

        DEVELOPER NAME: M.BALAVIGNESH

        Scope Of Implementation: Understanding about classmethod decorator.
'''

class ClassMethod:
    _names = ['Bala',
              'Deva',
              'Deepan']

    
    @classmethod
    def getnames(cls):
        return cls._names

if __name__ == "__main__":
    classm = ClassMethod()
    for x in classm.getnames():
        print(x)
    print(" ")
    classm.__class__._names = ['Bala',
                    'Maximus',
                    'Surendhar']
    for x in classm.getnames():
        print(x)