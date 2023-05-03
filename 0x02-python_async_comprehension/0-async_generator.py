#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def async_generator() -> float:
    """
    A coroutine that takes no arguments and loops ten times
    each time synchronously waiting 1 second and yields a
    random number between 0 and 10

    Parameters: None

    Returns: Random float values between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
