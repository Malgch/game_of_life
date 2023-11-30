class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} is located in {self.location}"

class Product:
    def __init__(self, name, price, company):
        self.name = name
        self.price = price
        self.company = company

    def get_price(self):
        return f"{self.name} costs {self.price}"

    def get_info(self):
        return f"{self.name} is produced by {self.company.name}"

company = Company("Apple", "California")
product = Product("iPhone", 222, company)

print(product.get_info())