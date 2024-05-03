#!/usr/bin/env python3
"""
calculate the sum of elements in a list containing
mixed data types (integers and floats).
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    calculate the sum of elements in the input list
    which may contain both integers and floats.
    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers.
    Returns:
        float: The sum of elements in the input list.
    """
    return sum(mxd_lst)
