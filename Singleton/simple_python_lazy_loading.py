# simple python-specific singleton implementation (lazy loading)
class Singleton:
    __instance = None

    # override the __new__ method to control how objects are created
    def __new__(cls):
        print ("Singleton init")
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance