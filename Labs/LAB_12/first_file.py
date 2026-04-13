#1. Декорування простих функцій:
from functools import wraps

from poetry.console.commands import self


def write_logs(func):
    def wrapper():
        print(f'{func.__name__} was called')
        return func()
    return wrapper

@write_logs
def hello_world() -> bool:
    print('hello world')
    return True

print(hello_world())

def write_logs_with_args(func):
    def wrapper(arg1, arg2):
        print(f'{func.__name__} was called with {arg1} and {arg2}')
        return func(arg1, arg2)
    return wrapper

@write_logs_with_args
def sum_func(a: int | float, b: int | float) -> int | float:
    return a + b

print(sum_func(1, 2))

#2. Параметризовані декоратори:

def count_calls(flag: bool):
    def wrapper(func):
        count = 0
        @wraps(func)
        def inner(*args, **kwargs):
            if flag:
                nonlocal count
                count += 1
                print(f'{func.__name__} was called {count} times')
            else:
                print(f'{func.__name__} was called')
            return func(*args, **kwargs)
        return inner
    return wrapper

@count_calls(True)
def test_func(arg1, arg2):
    return arg1, arg2

@count_calls(True)
def test_func2(arg1, arg2):
    return arg1, arg2

@count_calls(False)
def test_func3(arg1, arg2):
    return arg1, arg2

test_func(1, 2)
test_func(1, 2)
test_func(1, 2)

test_func2(1, 2)
test_func2(1, 2)
test_func2(1, 2)

test_func3(1, 2)
test_func3(1, 2)
test_func3(1, 2)

#3. Декорування в межах ООП:

def class_decorator(cls):
    original_init = cls.__init__

    def new_init(self1, *args, **kwargs):
        original_init(self1, *args, **kwargs)
        self1.bool_field = True

    cls.__init__ = new_init
    return cls

@class_decorator
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @count_calls(True)
    def sum_func(self):
        return self.arg1 + self.arg2


obj1 = MyClass(1, 2)
print(obj1.sum_func())
print(obj1.bool_field)