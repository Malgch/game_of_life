class SingletonMeta(type):
    __instances = {}

    def __init__(cls, name, bases, dct):
        """
        Override called during creation of the subtypes (actual Singletons)
        :param cls: The class instance that is being created. This is similiar to self for regular classes,
                    but since it is a metaclass, it acts on classes rather than instances.
        :param bases: A tuple of base classes from which the Singleton class inherits
        :param dct: A dictionary of the class attributes and methods
        """
        print("Metaclass init")
        super().__init__(name, bases, dct)
        cls.__instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls.__instances[cls]

# actual Singleton class
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        # initialize attributes here
        print("Singleton init")

    def logic(self):
        print("Singleton logic")

# below calls are not necessary for the Singleton instance to be created
# s = Singleton()
# s.logic()
