class Shape(object):
    # Create based on class name:
    def factory(cls):
        return object.__new__(cls)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")


c=Shape.factory(Circle)
s=Shape.factory(Square)
