#!/usr/bin/env python3
"""duck typing-first element of a sequence"""


from typing import Sequence, List, Any, Union


def safe_first_element(lst: Sequence[Any]) -> List[Union[Any, None]]:
    """if a list returns the first element else returns none"""
    if lst:
        return lst[0]
    else:
        return None
