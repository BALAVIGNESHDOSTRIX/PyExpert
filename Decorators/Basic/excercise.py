'''
    To extending the python function functionality without touching the implemented the code.
'''
from time import time

def timer(fun):
    def wrapper(*args, **kargs):
        start = time()
        result = fun(*args, **kargs)
        end = time()
        print("{x} Running time in Total Sec: ".format(x=fun.__name__), end-start)
        return result
    return wrapper

@timer
def hugeMul(n):
    return [x*42 for x in range(1, n+1)]

hugeMul(1728)

''' 
result:
hugeMul Running time in Total Sec:  0.00018453598022460938
'''

