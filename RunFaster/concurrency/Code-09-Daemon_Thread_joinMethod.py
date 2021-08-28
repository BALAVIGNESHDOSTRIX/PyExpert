'''
DEVELOPER NAME: BALAVIGNESH.M
IMPLEMETED DATE: 17-11-2018

                Implementation Details:
                    If the main thread is wait to complete the child thread process means we should use the
                    join() method so the main mehod will execute and main thread will wait.
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
tim.join()
