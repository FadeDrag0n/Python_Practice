import time


def find_prime(input_num):
    if input_num == 1:
        return 2
    num = 3
    count = 1
    while count < input_num:
        if is_prime(num):
            count += 1
        num += 2
    return num-2


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
    now = time.time()
    print(find_prime(10001))
    print(f'Time: {time.time() - now:.6f} s')