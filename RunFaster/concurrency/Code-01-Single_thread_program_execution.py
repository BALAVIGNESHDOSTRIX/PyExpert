'''
DEVELOPER NAME : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

import threading

class SingleThread:

    @staticmethod
    def ExtraInfo():
        print("Mark Antony is the next Emprorer of the Rome")

single = SingleThread()
s = threading.Thread(target = single.ExtraInfo())
s.start()
