'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading
import time

class OfficialThreadName:

    @staticmethod
    def GetThreadName():
        print(threading.currentThread().getName(),'Starting.....')
        time.sleep(3)
        print(threading.currentThread().getName(),'Exiting.....')

official = OfficialThreadName()

#default threadname declaration
tim = threading.Thread(target=official.GetThreadName)
servicethread = threading.Thread(name="servicethread",target=official.GetThreadName)
securitythread = threading.Thread(name="securitythread",target=official.GetThreadName)


#Thread starting sequence

tim.start()
securitythread.start()
servicethread.start()
