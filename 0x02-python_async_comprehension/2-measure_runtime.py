#!/usr/bin/env python3
""" Run time for four parallel comprehensions"""


import asyncio
from time import perf_counter
from importlib import import_module as find


async_comprehension = find('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that executes async_comprehension four times
    in parallel using asyncio.gather

    Parameters: None

    Returns: runtime of the function
    """
    start_time = perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = perf_counter()

    runtime = end_time - start_time

    return runtime
