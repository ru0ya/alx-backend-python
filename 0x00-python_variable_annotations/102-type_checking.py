#!/usr/bin/env python3

from typing import Tuple, Any, Union, List

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    zoomed_in: Tuple[Any, ...] = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
