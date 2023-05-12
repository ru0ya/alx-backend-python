#!/usr/bin/env python3

from typing import Tuple, Any, Union, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = []
    for item in lst:
        zoomed_in.extend([item] * factor)
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
