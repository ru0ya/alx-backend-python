#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies two floats"""
    def mult(x: float) -> float:
        return multiplier * x
    return mult
