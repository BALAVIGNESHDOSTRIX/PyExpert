"""
	Objective: To extend the thread class to custom thread class
"""

from threading import Thread
from time import sleep

class MaxThread(Thread):

	def run(self):
		sleep(2)

		print("This is called from the another thread")


# Example to pass the aruguments
class MaxThread_1(Thread):

	def __init__(self, delay):
		super(MaxThread_1, self).__init__()
		self.delay = delay

	def run(self):
		sleep(self.delay)

		print("This is called from the another thread")



if __name__ == '__main__':
	# thread = MaxThread() # create the thread
	# thread.start() # start the thread
	# thread.join() # wait to finish the thread

	thread = MaxThread_1(3) # create the thread
	thread.start() # start the thread
	thread.join() # wait to finish the thread


# https://superfastpython.com/extend-thread-class/