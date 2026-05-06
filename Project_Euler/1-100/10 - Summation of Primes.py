from time import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_sum(n):
    sum = 0
    for num in range(1, n + 1):
        if is_prime(num):
            sum += num
    return sum

start = time()

print(find_sum(2000000))


end = time() - start
print(f'{end:.5f} seconds')