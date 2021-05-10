####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "10/05/2021"               #
####################################

class Calculator:
    def add(*args):
        return sum(args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x 
        return result


class CalCulatorPool:
    _instance_pool = []

    def __call__(cls, size):
        for x in range(size):
            cls._instance_pool.append(CalCulatorPool())

    @staticmethod
    def factory():
        return CalCulatorPool()

    @classmethod
    def _aquire(cls):
        if not cls._instance_pool:
            return cls.factory()
        return cls._instance_pool.pop()

    @classmethod
    def _release(cls, instance):
        cls._instance_pool.append(instance)

    
    @classmethod
    def checker(cls):
        print(len(cls._instance_pool))



pool = CalCulatorPool()
pool(10)
pool.checker()