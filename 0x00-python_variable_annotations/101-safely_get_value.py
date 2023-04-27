#!/usr/bin/python3
"""takes two arguments: key and value and
accepts any dictionary like object"""

from typing import TypeVar, Any, Mapping, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """returns any dictionary like object"""
    if key in dct:
        return dct[key]
    else:
        return default
