# create a Singleton metaclass which will be used for instantiation of actual Singletons (lazy loading)
class SingletonMeta(type):
    # dictionary holding the instances of different Singletons
    __instances = {}

    def __call__(cls, *args, **kwargs):
        # single instance of a specific class already created?
        print("Metaclass call")
        if cls not in cls.__instances:
            # create a new instance of the singleton by calling the parent's __call__ method
            instance = super().__call__()
            cls.__instances[cls] = instance

        # return already created instance
        return cls.__instances[cls]

# actual Singleton implementation
class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        print("Singleton logic")

s1 = Singleton()
s2 = Singleton()
s2.some_logic()
print(s1 is s2)