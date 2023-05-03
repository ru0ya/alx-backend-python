#!/usr/bin/env python3
"""Async Comprehensions"""


import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """
    coroutine that takes 10 random numbers using an async
    comprehension over async_generator

    Parameters: None

    Returne: 10 random numbers
    """
    for i in range(10):
        result = [number async for number in async_generator()]
    return result
