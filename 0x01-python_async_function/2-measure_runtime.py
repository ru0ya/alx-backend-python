#!/usr/bin/env python3
"""Measure runtime"""


from time import perf_counter
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function with integers as arguments that
    measures total execution time for a function
    wait_n(n, max_delay)

    Parameters: n(int), max_delay(int)

    Returns: total_time / n
    """
    start_time = perf_counter()

    asyncio.run(wait_n(n, max_delay))

    stop_time = perf_counter()

    total_time = stop_time - start_time

    return (total_time / n)
