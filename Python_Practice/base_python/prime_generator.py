def prime_generator():
    num = 0
    while True:
        num += 1
        if is_prime(num):
            yield num


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


gen = prime_generator()
print([next(gen) for _ in range(5)])