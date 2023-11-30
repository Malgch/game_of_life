class SingletonMeta(type):
    __instances = {}

    def __new__(cls, *args, **kwargs):
        """
        Override called during creation of the subtypes (actual Singletons)
        :param cls: The class instance that is being created. This is similiar to self for regular classes,
                    but since it is a metaclass, it acts on classes rather than instances.
        :param args: A variable-length argument list. It allows the __new__ method to accept any number of arguments
        :param kwargs: A varaible-length keyword argument dictionary. It allows the __new__ method to accept any
                        number of keyword arguments
        """
        print("Metaclass new")
        new_class = super().__init__(cls, *args, **kwargs)
        # eager loading of the Singleton instance
        cls.__instances[new_class] = super(SingletonMeta, new_class).__class__()
        return  new_class

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
