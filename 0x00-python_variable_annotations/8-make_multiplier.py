#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(x: float) -> Callable[[float], float]:
    """returns a function that multiplies two floats"""
    def multiplier(y: float) -> float:
        return x * y
    return multiplier
