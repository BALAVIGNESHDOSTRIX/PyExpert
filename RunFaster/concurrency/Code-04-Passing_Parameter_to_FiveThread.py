'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading

class FiveThreadargs:

    def FindSquareValues(self,num):
        print("The SquareValue of {y}".format(y=num))
        print("The Result is:", num * num)

five = FiveThreadargs()

thread_list = [] #Thread list for tracking the each seprate Thread details

for i in range(5):
    tim = threading.Thread(target=five.FindSquareValues,args=(10,))
    thread_list.append(tim)
    tim.start()
