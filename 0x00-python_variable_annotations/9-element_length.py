#!/usr/bin/env python3
'''Task 9's module - Let's duck type an iterable object.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''This computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
