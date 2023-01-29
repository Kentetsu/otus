import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_triangle_correct_input():
    Triangle(1, 1, 1)
    Triangle(10, 15, 10)
    Triangle(1.5, 2, 1.5)


def test_triangle_wrong_input():
    with pytest.raises(ValueError):
        Triangle(1, 1, 2)
    with pytest.raises(ValueError):
        Triangle(-1, 1, 1)
    with pytest.raises(ValueError):
        Triangle('14', 1, 38)


def test_square_correct_input():
    Square(1)
    Square(38)
    Square(6.2)


def test_square_wrong_input():
    with pytest.raises(ValueError):
        Square(None)
    with pytest.raises(ValueError):
        Square('str')


def test_rectangle_correct_input():
    Rectangle(1, 1)
    Rectangle(5, 25)
    Rectangle(1.4, 7.2)


def test_rectangle_wrong_input():
    with pytest.raises(ValueError):
        Rectangle(None, None)
    with pytest.raises(ValueError):
        Rectangle('str', 'str')


def test_circle_correct_input():
    Circle(1)
    Circle(250)
    Circle(6.2)


def test_circle_wrong_input():
    with pytest.raises(ValueError):
        Circle(None)
    with pytest.raises(ValueError):
        Circle('str')
