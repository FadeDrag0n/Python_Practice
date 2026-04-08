# Напиши рекурсивную функцию вычисления чисел Фибоначчи
from functools import lru_cache


@lru_cache
def fib(n):
    if n == 1: return 1
    if n < 1: return 0
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(7))  # 13
print(fib(40))