'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading

class FiveThread:

    @staticmethod
    def Buggatti():
        print("Buggatti is the world super fast car its maximum speed is 458 km/h above")

thread_list = []
five = FiveThread()

for i in range(5):
    tim = threading.Thread(target = five.Buggatti())
    thread_list.append(tim)
    #print(thread_list)
    tim.start()
