import time

def find_dif(num):
    square_of_sum = (num * (num + 1) / 2) ** 2
    sum_of_squares = num * (num + 1) * (2 * num + 1) // 6
    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    now = time.time()
    print(find_dif(10000))
    passed_time = (time.time() - now)
    print(f'{passed_time:.6f}')