'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''
import threading
import time

class ThreadName:

    @staticmethod
    def GetThreadName():
        print(threading.currentThread().getName(),'Strating....')
        time.sleep(2)
        print(threading.currentThread().getName(),'Exiting.....')

thname = ThreadName()

tim = threading.Thread(target=thname.GetThreadName)
tim.start()
