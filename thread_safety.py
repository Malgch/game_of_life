from threading import Lock
from threading import Thread

class Counter(object):
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        self.lock.acquire()
        # critical section
        self.counter += 1
        self.lock.release()