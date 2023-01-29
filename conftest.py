import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle

DEFAULT_SIZE = 1


@pytest.fixture()
def default_figures():
    def_circle = Circle(DEFAULT_SIZE)
    def_rectangle = Rectangle(DEFAULT_SIZE, DEFAULT_SIZE)
    def_square = Square(DEFAULT_SIZE)
    def_triangle = Triangle(DEFAULT_SIZE, DEFAULT_SIZE, DEFAULT_SIZE)

    return def_circle, def_rectangle, def_square, def_triangle
