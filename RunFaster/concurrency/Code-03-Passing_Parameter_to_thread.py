'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading

class SingleThreadparameter:

    def AddSum(self,num1,num2):
        print("The Given numbers Are {x} and {y}".format(x=num1,y=num2))
        print("The Result is:", num1 + num2)


single = SingleThreadparameter()

tim = threading.Thread(target=single.AddSum,args=(20,30))
tim.start()
