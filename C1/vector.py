from collections import namedtuple
from math import hypot

Vector = namedtuple("Vector", ["x", "y"])

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
if __name__ == "__main__":
    a, b = Vector(1, 2), Vector(3, 4)
    print(a)
    print(b)

    print(a + b)
    print(a * -1)
