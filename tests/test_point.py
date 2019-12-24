"""Test point creation."""
import numpy as np

from pytest import fixture, mark
from simgeo.point import Point


@fixture(scope="function")
def point2d():
    return Point(1, -2)


def test_create_point(point2d):
    assert point2d[0] == 1
    assert point2d[1] == -2


def test_selection_point_coordinate_section():
    point = Point(1, 2, 3, 4, 5)

    coords = point[1:-1]
    assert np.array_equal(coords, np.array([2, 3, 4]))


def test_point_equal(point2d):
    assert point2d == Point(1, -2)


def test_point_not_equal(point2d):
    assert point2d != Point(-2, 1)


@mark.parametrize(
    "scale, expected",
    [
        [
            10, Point(10, -20),
        ],
        [
            -3, Point(-3, 6),
        ],
    ],
)
def test_point_multiply(point2d, scale, expected):
    scaled_point = point2d * scale
    assert scaled_point == expected
