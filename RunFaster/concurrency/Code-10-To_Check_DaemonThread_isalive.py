'''
DEVELOPER NAME: BALAVIGNESH.M
IMPLEMETED DATE: 17-11-2018

'''


import threading
import time

class DaemonThread:

    @staticmethod
    def GetThreadInfo():
        print(threading.currentThread().getName(),'Starting......')
        time.sleep(10)
        print(threading.currentThread().getName(),'Exiting......')

daemon = DaemonThread()

tim = threading.Thread(target=daemon.GetThreadInfo)
tim.setDaemon(True)
tim.start()
tim.join(2)
print("Check Is the Thread is Alive : ",tim.isAlive())
print("Check Is the Thread was Daemon : " ,tim.isDaemon())
