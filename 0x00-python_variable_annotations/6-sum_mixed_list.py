#!/usr/bin/env python3
"""takes a mixed list as argument
and returns sum as a float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of a mixed list"""
    return sum(mxd_lst)
