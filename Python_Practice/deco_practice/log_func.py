def log_func(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'func {func.__name__} args {args} kwargs {kwargs}')
        return res
    return inner


@log_func
def my_func(*args, **kwargs):
    value_list = list(value for key, value in kwargs.items())
    return sum(args) + sum(value_list)




my_func(1, 3, 4, 5, 2, c = 5, d = 125)
