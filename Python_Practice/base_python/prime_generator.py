from typing import Generator

def prime_generator() -> Generator[int, None, None]:
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


gen = prime_generator()
print([next(gen) for _ in range(5)])