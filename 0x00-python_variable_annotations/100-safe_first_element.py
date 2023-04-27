#!/usr/bin/env python3
"""duck typing-first element of a sequence"""


from typing import Sequence, Any, Union, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """if a list returns the first element else returns none"""
    if lst:
        return lst[0]
    else:
        return None
