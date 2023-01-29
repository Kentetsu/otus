import pytest


def test_triangle_add_area(default_figures):
    assert default_figures[3].add_area(default_figures[0]) == 3.5746053554820123
    assert default_figures[3].add_area(default_figures[1]) == 1.4330127018922192
    assert default_figures[3].add_area(default_figures[2]) == 1.4330127018922192
    assert default_figures[3].add_area(default_figures[3]) == 0.8660254037844386


def test_circle_add_area(default_figures):
    assert default_figures[0].add_area(default_figures[0]) == 6.283185307179586
    assert default_figures[0].add_area(default_figures[1]) == 4.141592653589793
    assert default_figures[0].add_area(default_figures[2]) == 4.141592653589793
    assert default_figures[0].add_area(default_figures[3]) == 3.5746053554820123


def test_rectangle_add_area(default_figures):
    assert default_figures[1].add_area(default_figures[0]) == 4.141592653589793
    assert default_figures[1].add_area(default_figures[1]) == 2
    assert default_figures[1].add_area(default_figures[2]) == 2
    assert default_figures[1].add_area(default_figures[3]) == 1.4330127018922192


def test_square_add_area(default_figures):
    assert default_figures[1].add_area(default_figures[0]) == 4.141592653589793
    assert default_figures[1].add_area(default_figures[1]) == 2
    assert default_figures[1].add_area(default_figures[2]) == 2
    assert default_figures[1].add_area(default_figures[3]) == 1.4330127018922192

