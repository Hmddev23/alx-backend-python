#!/usr/bin/env python3
"""
create a tuple with a key-value pair where the value is squared.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a key-value pair where the value is squared.
    Args:
        k (str): The key.
        v (Union[int, float]): The value number.
    Returns:
        Tuple[str, float]: A tuple containing the key, value.
    """
    return (k, v**2)
