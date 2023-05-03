#!/usr/bin/env python3
""" Run time for four parallel comprehensions"""


import asyncio
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())

    end_time = perf_counter()

    runtime = end_time - start_time

    return runtime
