#!/usr/bin/env python3
"""
imports wait_random from 0-basic_async_syntax
A normal function that returns a asyncio.Task
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer and returns asyncio.Task

    Parameters: max_delay(int)

    Returns: asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
