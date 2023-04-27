#!/usr/bin/env python3
"""duck typing an iterable object"""

from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
