import threading

class ThreadSafeSingleton():
    __instance = None
    # class-level lock for thread safety
    _lock = threading.Lock()

    # __new__ thread-safe implementation
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            # if not cls.__instance: # checks if instance is falsy
            if cls.__instance is None: # cheks if instance is specifically None
                # create instance
                cls.__instance = super().__new__(cls)

            return cls.__instance # releases the lock automatically


s = ThreadSafeSingleton()
