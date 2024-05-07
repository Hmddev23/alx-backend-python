#!/usr/bin/env python3
"""
asynchronously generate a list of random floating-point number
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    asynchronously generate a list of random floating-point
    numbers using an asynchronous comprehension.
    Returns:
        List[float]: A list of random floating-point numbers.
    """
    return [random async for random in async_generator()]
