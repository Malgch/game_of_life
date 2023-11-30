# GoF (Gang of Four) implementation
class ClassicSingleton:
    # class-level variable to hold the Singleton instance
    __instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        raise RuntimeError("Call get_instance() instead")

    # allows to fetch the single instance of Singleton
    @classmethod
    def get_instance(cls):
        # check if singleton instance was alrady created
        if not cls.__instance: # lazy loading
            # create a singleton instance
            print("Singleton get_instance()")
            cls.__instance = cls.__new__(cls)

        # return the existing instance of Singleton
        return cls.__instance


s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()
print(s1 is s2)
print(s1)
print(s2)

