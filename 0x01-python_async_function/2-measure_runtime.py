#!/usr/bin/env python3
"""
measure the average time taken to execute a function.
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure the average time taken to execute 'wait_n'
    for 'n' number of times with a maximum delay of 'max_delay'.
    Parameters:
    - n (int): The number of times to execute 'wait_n'.
    - max_delay (int): The maximum delay in seconds for each execution of 'wait_n'.
    Returns:
    - float: The average time taken for each execution of 'wait_n'.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
