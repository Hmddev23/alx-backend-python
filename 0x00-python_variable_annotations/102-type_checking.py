#!/usr/bin/env python3
"""
repeat the elements of a tuple in a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    repeat the elements of a tuple in a specified number of times.
    Args:
        lst (Tuple): The tuple.
        factor (int, optional): The factor by which to repeat in.
    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
