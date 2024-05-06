#!/usr/bin/env python3
"""
creates tasks waiting for each other in random delay.
"""
import random
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    creates 'n' tasks, each waiting for a random delay.
    Parameters:
    - n (int): The number of tasks to create.
    - max_delay (int): The maximum delay in seconds for each task.
    Returns:
    - List[float]: A list of delays that were waited.
    """
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*delays))
