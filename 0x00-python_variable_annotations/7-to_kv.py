#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a string and square of an int/float"""
    return (k, v**2)
