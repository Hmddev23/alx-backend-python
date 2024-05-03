#!/usr/bin/env python3
"""
retrieve a value from a mapping.
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    retrieve a value from a mapping.
    Args:
        dct (Mapping): A mapping.
        key (Any): The key from the mapping.
        default (Union[T, None], optional): The default value to return.
    Returns:
        Union[Any, T]: The value associated with the key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
