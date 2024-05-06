#!/usr/bin/env python3
"""
wait for a random amount of time in seconds.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random amount of time between 0 and max_delay seconds.
    Parameters:
    - max_delay (int): The maximum delay in seconds (default is 10).
    Returns:
    - float: The actual delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
