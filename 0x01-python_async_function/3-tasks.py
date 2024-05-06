#!/usr/bin/env python3
"""
create an async task that waits for a random delay.
"""
import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create an async task that waits for a random delay.
    Parameters:
    - max_delay (int): The maximum delay in seconds.
    Returns:
    - asyncio.Task: An async task object.
    """
    return asyncio.create_task(wait_random(max_delay))
