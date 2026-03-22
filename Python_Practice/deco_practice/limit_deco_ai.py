import time
from typing import Callable
from functools import wraps


def limit_calls_deco(limit: int):
    def wrapper(func: Callable):
        counter = 0  # теперь внутри замыкания

        @wraps(func)
        def inner(*args, **kwargs) -> int | str:
            nonlocal counter
            counter += 1

            if counter <= limit:
                return func(*args, **kwargs)
            else:
                return 'Limit is passed'

        return inner
    return wrapper


@limit_calls_deco(1)
def my_func(sleep_time: int) -> int:
    print('my_func called')
    time.sleep(sleep_time)
    return 123


@limit_calls_deco(2)
def my_func2(sleep_time: int) -> int:
    print('my_func2 called')
    time.sleep(sleep_time)
    return 500

print(my_func(1))
print(my_func(1))
print(my_func(1))
print(my_func2(1))
print(my_func2(1))
print(my_func2(1))
