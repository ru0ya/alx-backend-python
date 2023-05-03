#!/usr/bin/env python3

"""Async Comprehensions"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that takes 10 random numbers using an async
    comprehension over async_generator

    Parameters: None

    Returns: 10 random numbers
    """
    result = [number async for number in async_generator()]
    return result
