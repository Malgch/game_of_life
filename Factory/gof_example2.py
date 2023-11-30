from abc import ABC, abstractmethod

# Step 1: Create a Shape contract (interface)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Implement the Shape contract in concrete classes
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

# Step 3: Create a Factory contract (interface)
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self) -> Shape:
        pass

# Step 4: Implement the Factory contract in concrete classes
class RectangleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Rectangle()

class CircleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Circle()

# Step 5: Client code
def client_code(factory: ShapeFactory):
    shape = factory.create_shape()
    print(shape.draw())

# Creating shapes using factories
rectangle_factory = RectangleFactory()
circle_factory = CircleFactory()

client_code(rectangle_factory)  # Output: Drawing a Rectangle
client_code(circle_factory)     # Output: Drawing a Circle
