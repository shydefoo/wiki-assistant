from time import time
from functools import wraps


def time_query(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        start = time()
        val = func(*args, **kwargs)
        end = time()
        return val, end-start
    return _wrapper
