'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading
import time

class serviceThread:

    @staticmethod
    def serviceThreadName():
        print(threading.currentThread().getName(),'Starting....')
        time.sleep(2)
        print(threading.currentThread().getName(),'Exiting....')

class securityThread:

    @staticmethod
    def securityThreadName():
        print(threading.currentThread().getName(),'Strating....')
        time.sleep(2)
        print(threading.currentThread().getName(),'Exiting....')

service = serviceThread()
security = securityThread()

tim = threading.Thread(target=service.serviceThreadName)
service_thread = threading.Thread(name="ServiceThread",target=service.serviceThreadName)
security_thread = threading.Thread(name="securitythread",target=security.securityThreadName)

service_thread.start()
security_thread.start()
tim.start()
