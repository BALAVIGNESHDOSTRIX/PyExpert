'''
DEVELOPER NAME: BALAVIGNESH.M
IMPLEMETED DATE: 17-11-2018

            Implementation Details:
                    When creating the Daemon thread the Daemon thread is will not block by the another threads 
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
print("Check Is the Thread was Daemon : " ,tim.isDaemon())
tim.start()
