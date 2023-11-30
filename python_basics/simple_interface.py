# required for abstract class
from abc import ABC, abstractmethod

# Interface contract. Children have to implement all of the abstract methods.
# Interface methods have no implementation - `pass`

class Interface(ABC):
    @abstractmethod
    def first_method(self):
        pass

class FirstClass(Interface):
    def first_method(self):
        print("First interface implementation")

class SecondClass(Interface):
    def first_method(self):
        print("Second interface implementation")

# type hinting
def process_interface(obj: Interface):
    obj.first_method()
    print("Correct interface implementation")

first_obj = FirstClass()
first_obj.first_method()

second_obj = SecondClass()
second_obj.first_method()

process_interface(first_obj)
process_interface(second_obj)
