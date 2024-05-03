#!/usr/bin/env python3
"""
define a function to calculate the sum of elements in a list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    calculate the sum of elements in the input list.
    Args:
        input_list (List[float]): A list of floating-point numbers.
    Returns:
        float: The sum of elements in the input list.
    """
    return sum(input_list)
