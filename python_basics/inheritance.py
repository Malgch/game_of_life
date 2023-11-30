# Base (parent) class
class Console:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(self.name)

# Derived (child) classes
class Xbox(Console):
    def info(self):
        print(self.name, "Produced by Microsoft")

class PlayStation(Console):
    def info(self):
        print(self.name, "Produced by Sony")

xbox = Xbox("X360")
ps = PlayStation("PS5")

xbox.info()
ps.info()

