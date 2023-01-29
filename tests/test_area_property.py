import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_triangle_area():
    assert Triangle(2, 2, 2).area == 1.7320508075688772


def test_rectangle_area():
    assert Rectangle(2, 1).area == 2


def test_square_area():
    assert Square(2).area == 4


def test_circle_area():
    assert Circle(2).area == 12.566370614359172

