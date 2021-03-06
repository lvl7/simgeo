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


def test_add_points(point2d):
    point_other = Point(-4, 10)
    resolution_point = point_other + point2d
    assert resolution_point == Point(-3, 8)


def test_iadd_point(point2d):
    point_other = Point(-4, 10)
    point2d += point_other
    assert point2d == Point(-3, 8)


def test_subtract_points(point2d):
    point_other = Point(-4, 10)
    resolution_point = point2d - point_other
    assert resolution_point == Point(5, -12)


def test_isub_point(point2d):
    point_other = Point(-4, 10)
    point2d -= point_other
    assert point2d == Point(5, -12)


def test_specify_type_of_coordinates():
    point = Point(1, 2, 3, dtype=np.float64)
    assert all((isinstance(coord, np.float64) for coord in point))


def test_distance():
    assert Point(-1, -1).distance(Point(-1, 1)) == 2
