#!/usr/bin/env python3
"""
This script defines a higher-order function to create
a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    create a multiplier function.
    Args:
        multiplier (float): The multiplier to be used in the function.
    Returns:
        Callable[[float], float]: return the product value.
    """

    def mult(m: float) -> float:
        """
        Multiply a given number by the multiplier.
        Args:
            m (float): The number to be multiplied.
        Returns:
            float: The result of the given number by the multiplier.
        """
        return m * multiplier

    return mult
