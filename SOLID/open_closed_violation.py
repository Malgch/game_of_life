class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return shape.radius ** 2 * 3.14
        elif isinstance(shape, Square):
            return shape.side ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Square:
    def __init__(self, side):
        self.side = side
