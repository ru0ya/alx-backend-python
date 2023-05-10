#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    imports wait_random and creates an async routine

    parameters:
    n(int): number of times to spawn max_delay
    max_delay(int): maximum amount of time to delay in sec

    Returns:
    list of all the delays as float values
    """
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))
    for delay in asyncio.as_completed(tasks):
        result = await delay
        delays.append(result)
    return delays
