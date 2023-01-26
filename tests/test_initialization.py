from src.Triangle import Triangle
import pytest


def test_initialization_correct_input():
    triangle1 = Triangle(1, 1, 1)
    triangle2 = Triangle(1, 1, 2)
    triangle3 = Triangle(1, 1, 3)

