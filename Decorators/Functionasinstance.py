'''
        IMPLEMENTED DATE: 23/06/2019

        DEVELOPER NAME: M.BALAVIGNESH

        Scope of Implementation: To understanding the functional flow of when function
                                 maked as a instance without creating the instance
'''

import random

class RandomChoice:
    def __init__(self, func):
        self._func = func
        self.memory = []

    def __call__(self):
        reval = self._func()
        self.memory.append(reval)

    def getMemoryValue(self):
        return self.memory


@RandomChoice
def getRandChoice():
    ranval = random.choice([1,2,374,343,234,829,672,9392,199,920,1242])
    return ranval

if __name__ == "__main__":
    print(getRandChoice())
    print(getRandChoice.getMemoryValue())
    print(getRandChoice())
    print(getRandChoice.getMemoryValue())
    