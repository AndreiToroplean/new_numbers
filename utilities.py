import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        rtn = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start}s to run.")
        return rtn

    return wrapper
