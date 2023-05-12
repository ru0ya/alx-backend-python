#!/usr/bin/env python3

from typing import Tuple, Any, Union, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: Tuple[int, ...] = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array: Tuple[int, ...] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
