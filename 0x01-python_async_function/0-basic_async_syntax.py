#!/usr/bin/env python3
"""basics of async"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (inclusive) seconds and
    return the delay time as a float.

    Parameters:
    max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
    float: The delay time in seconds as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
