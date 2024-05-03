#!/usr/bin/env python3
"""
compute the length of elements in an iterable of sequences.
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    compute the length of elements in an iterable of sequences.
    Args:
        lst (Iterable[Sequence]): An iterable of sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples.
    """
    return [(i, len(i)) for i in lst]
