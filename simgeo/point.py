"""Point implementation."""
from typing import Union, overload

import numpy as np


class Point:
    """
    Point object.

    Can have any number of dimensions.
    """

    def __init__(self, *coords: int):
        r"""
        Initialize points.

        Args:
            \*coords: coordinates of point
        """
        self.coords = self._set_coords(*coords)

    @overload
    def __getitem__(self, coord_index: slice) -> np.array:
        """
        For slice coord_index np.array of coordinates should be returned.

        Args:
            coord_index: slice of coordinates

        Returns:
            array of corresponding point coordinates

        """

    def __getitem__(self, coord_index: int) -> Union[float, int]:  # noqa: F811
        """
        Get selected point coordinate.

        Args:
            coord_index: index of point coordinate

        Returns:
            selected point coordinate
        """
        return self.coords[coord_index]

    def _set_coords(self, *coords):
        r"""
        Create numpy array from given coordinates.

        Args:
            \*coords: coordinates of point

        Returns:
             numpy array filled with coordinates

        """
        return np.array(coords)
