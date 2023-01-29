import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_triangle_perimeter():
    assert Triangle(2, 2, 2).perimeter == 6


def test_rectangle_perimeter():
    assert Rectangle(2, 1).perimeter == 6


def test_square_perimeter():
    assert Square(2).perimeter == 8


def test_circle_perimeter():
    assert Circle(2).perimeter == 12.566370614359172
