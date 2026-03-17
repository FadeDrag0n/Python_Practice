# Блок 3. Просунуті механізми передачі аргументів

# 3.1. Гнучкість викликів:

def print_numbers(int1 = 1, int2 = 2, int3 = 3, int4 = 4):
    print(int1, int2, int3, int4)
print_numbers(45, 124)
print_numbers(23, 12, 124, 344)
print_numbers(12, int2 = 1234, int3 =123)

def print_numbers2(*args):
    print(args)
print_numbers2(34, 4231, 43, 12)
def print_numbers3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_numbers3(name='Artem', age='19', surname='Polovyk')

# 3.2. Розпакування:

def unboxing_example(value1, value2, value3):
    print(max(sum(value1), sum(value2), sum(value3)))
list1 = [[100, 200], [50, 30, 120], [500]]
unboxing_example(*list1)

def unboxing_example2(int_ = 5, **kwargs):
    print(kwargs)
    print(int_)
dict1 = {'a': 100, 'b': 200}
unboxing_example2(**dict1)

# 3.3 Обмеження виклику

def limited_function(a, *b, c):
    print(a)
    print(b)
    print(c)
#limited_function(1, (2,34), 3) TypeError: limited_function() missing 1 required keyword-only argument: 'c'
limited_function(1, 2, 3, 4, 5, c=3)

#Блок 4. Аналітичні задачі (Case Studies)

# 4.1. Пастка мутабельних аргументів:
#def func1(a, list_=[])

def func1(a, list_=None):
    if list_ is None:
        list_ = []
    list_.append(a)
    return list_
print(func1(1))
print(func1(2))
print(func1(3))

#  4.2. Імутабельні типи за замовчуванням:

def func2(a, t=()):
    return a in t
print(func2(1))
print(func2(2))
print(func2(3, (1, 2, 3)))

# 4.3. Складні сигнатури:

def f(a, *, b):
    ...
def f2(a, *c, b):
    ...
def f333(x, *y, z, **w):
    ...
f(1, b = 1)
f2(1, 1, 2, 3, b=5)
f333(1, 1, 2, 3, z=5, a=100, b=200)