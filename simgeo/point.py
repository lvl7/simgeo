"""Point implementation."""
from typing import Union, overload

import numpy as np

Coord = Union[int, float]


class Point:
    """
    Point object.

    Can have any number of dimensions.
    """

    def __init__(self, *coords: Union[Coord, np.ndarray], dtype=None):
        r"""
        Initialize points.

        Args:
            \*coords: coordinates of point
            dtype: ensure type of coordinates. See ``numpy.dtype``.
        """
        self.coords = self._set_coords(*coords, dtype=dtype)

    @overload
    def __getitem__(self, coord_index: slice) -> np.ndarray:
        """
        For slice coord_index np.array of coordinates should be returned.

        Args:
            coord_index: slice of coordinates

        Returns:
            array of corresponding point coordinates

        """

    def __getitem__(self, coord_index: int) -> Coord:  # noqa: F811
        """
        Get selected point coordinate.

        Args:
            coord_index: index of point coordinate

        Returns:
            selected point coordinate
        """
        return self.coords[coord_index]

    def __add__(self, other: "Point") -> "Point":
        """
        Create new point with sum of ``self`` and ``other`` corresponding coordinates.

        Args:
            other: point that will be added to ``self``

        Returns:
            new point with sum of coordinates

        """
        if isinstance(other, Point):
            return Point(self.coords + other.coords)

        return NotImplemented

    def __iadd__(self, other: "Point") -> "Point":
        """
        Add corresponding coordinates from ``other`` to ``self``.

        Args:
            other: point whom coordinates will be added to self

        Returns:
            modified point

        """
        if isinstance(other, Point):
            self.coords += other.coords
            return self

        return NotImplemented

    def __sub__(self, other: "Point") -> "Point":
        """
        Create new point with subtract of ``self`` and ``other`` corresponding coordinates.

        Args:
            other: point that will be subtracted from ``self``

        Returns:
            new point with subtracted coordinates

        """
        if isinstance(other, Point):
            return Point(self.coords - other.coords)

        return NotImplemented

    def __isub__(self, other: "Point") -> "Point":
        """
        Subtract corresponding ``other`` coordinates from ``self``.

        Args:
            other: point whom coordinates will be subtracted from self

        Returns:
            modified point

        """
        if isinstance(other, Point):
            self.coords -= other.coords
            return self

        return NotImplemented

    def __mul__(self, other: Union[int, float]) -> "Point":
        """
        Scale point.

        Args:
            other: magnitude

        Returns:
            new scaled point

        """
        if isinstance(other, (int, float)):
            return Point(self.coords * other)

        return NotImplemented

    def __eq__(self, other: "Point") -> bool:
        """
        Check if given point has same coordinates.

        Args:
            other: point to compare with

        Returns:
            true - ``other`` has same coordinate,
            false - anyway

        """
        if isinstance(other, Point):
            return np.array_equal(self.coords, other.coords)

        return NotImplemented

    def _set_coords(self, *coords, dtype: np.dtype = None):
        r"""
        Create numpy array from given coordinates.

        Args:
            \*coords: coordinates of point. Could be:
                      - list of numbers
                      - list of one np.ndarray
            dtype: ensure type of coordinates. See ``numpy.dtype``.

        Returns:
             numpy array filled with coordinates

        """
        if len(coords) == 1 and isinstance(coords[0], np.ndarray):
            return np.copy(coords[0])

        return np.array(coords, dtype=dtype)

    def distance(self, other: "Point") -> float:
        """
        Calculate Euclidea distance between given point.

        Args:
            other: point to which distance will be mesured

        Returns:
            distance to ``other``
        """
        return float(
            np.sqrt(np.sum(np.square((self - other).coords))))
