import time
import typing

def limit_calls_deco(limit: int):
    def wrapper(func: typing.Callable):
        def inner(*args, **kwargs):
            global my_func_counter
            my_func_counter += 1
            if my_func_counter <= limit:
                res = func(*args, **kwargs)
                return res
            else:
                return f'Limit is passed'
        return inner
    return wrapper


@limit_calls_deco(1)
def my_func(sleep_time: int):
    print('my_func called')
    time.sleep(sleep_time)
    return 123

my_func_counter = 0
print(my_func(1))
print(my_func(1))
print(my_func(1))