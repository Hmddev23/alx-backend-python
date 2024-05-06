#!/usr/bin/env python3
"""
waits for 'n' random delays
"""
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    waits for 'n' random delays, each delay being a random
    amount of time between 0 and 'max_delay' seconds.
    Parameters:
    - n (int): The number of delays to wait for.
    - max_delay (int): The maximum delay in seconds.
    Returns:
    - List[float]: A list containing the actual delays
    that were waited, sorted in ascending order.
    """
    listDelays = []
    for _ in range(n):
        listDelays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*listDelays))
