#!/usr/bin/python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(x: float) -> Callable[[float], float]:
    def multiplier(y: float) -> float:
        return x * y 
    return multiplier

