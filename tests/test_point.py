"""Test point creation."""
import numpy as np

from simgeo.point import Point


def test_create_point():
    point = Point(1, 2)

    assert point[0] == 1
    assert point[1] == 2


def test_selection_point_coordinate_section():
    point = Point(1, 2, 3, 4, 5)

    coords = point[1:-1]
    assert np.array_equal(coords, np.array([2, 3, 4]))
