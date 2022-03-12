import threading

class ThreadSafeDict(set) :
    def __init__(self, * args, **kwargs) :
        super.__init__(self, * args, **kwargs)
        self._lock = threading.Lock()

    def __enter__(self) :
        self._lock.acquire()
        return self

    def __exit__(self, type, value, traceback) :
        self._lock.release()