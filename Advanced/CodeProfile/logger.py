####################################
# Author: "BALAVIGNESH"            #
# Maintainer: "BALAVIGNESH"        #
# License: "CC0 1.0 Universal"     #
# Date: "25/04/2021"               #
####################################

import os, logging, sys
from datetime import datetime


class log(object):
    def __init__ (self, *args, **kwargs):
        # store arguments passed to the decorator
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def newf(*args, **kwargs):
            print(args, kwargs)

            #the 'self' for a method function is passed as args[0]
            slf = args[0]

            # replace and store the attributes
            saved = {}
            for k,v in kwargs.items():
                if hasattr(slf, k):
                    saved[k] = getattr(slf,k)
                    setattr(slf, k, v)
                    
            start = datetime.now()                #start time
            func_exec = func(*args, **kwargs)     #function call
            func_name = func.__name__             #function name
            end = datetime.now()                  #end time
            timx = end.timestamp() - start.timestamp()
            ''' Message '''
            message = """ Function: {func} 
                        Execution Time: {extim}
                        Address: {address}
                        Memory: {memory} Bytes
                        Date: {date}""".format(func=func_name, extim=timx,
                                                address=func.__repr__, memory=sys.getsizeof(func),
                                                date=start)
            
            cwd = os.getcwd()
            folder = "Logs"
            path = os.path.join(cwd, folder)
            try:
                os.mkdir(path)
            except:
                logging.basicConfig(filename="{}/function.log".format(path),level=logging.DEBUG)
                logging.debug(message)

            return func_exec
        return newf