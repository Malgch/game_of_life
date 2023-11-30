class IPrinter:
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing")

class Scanner(IScanner):
    def print(self):
        print("Scanning")

class Copier(IPrinter, IScanner):
    def scan(self):
        print("Scanning")

    def print(self):
        print("Priniting")

    def copy(self):
        print("Copying")
        self.scan()
        self.print()

class Fax(IFax):
    def fax(self):
        print("Faxing")
