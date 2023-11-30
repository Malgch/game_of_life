from abc import ABC, abstractmethod

# Define the Shape contract
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Define the Rectangle class that implements the Shape contract
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

# Define the Circle class that implements the Shape contract
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# Define the Factory contract
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

# Define the RectangleFactory class that implements the Factory contract
class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()

# Define the CircleFactory class that implements the Factory contract
class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

# Example usage
rectangle_factory = RectangleFactory()
rectangle = rectangle_factory.create_shape()
rectangle.draw()

circle_factory = CircleFactory()
circle = circle_factory.create_shape()
circle.draw()
