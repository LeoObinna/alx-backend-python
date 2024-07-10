#!/usr/bin/env python3
'''Task 2's module - Run time for four parallel comprehensions.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehensive').async_comprehensive


async def meaure_runtime() -> float:
    '''This executes async_comprehensive 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehensive() for _ in range(4)))
    return time.time() -
