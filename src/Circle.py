from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        if not (type(radius) == int or type(radius) == float):
            raise ValueError
        self.radius = radius

    @property
    def perimeter(self):
        return 2*pi*self.radius

    @property
    def area(self):
        return pi * (self.radius ** 2)

