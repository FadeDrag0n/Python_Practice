import time


# def smallest_multiple_1(multiple_limit):
#     num = 20
#     while True:
#         flag = True
#         for val in range(multiple_limit, 6, -1):
#             if num % val != 0:
#                 flag = False
#                 break
#         if flag:
#             break
#         num += 2
#     return num

# def smallest_multiple_2(multiple_limit):
#     dividers = range(6, multiple_limit+1)
#     n = 20
#     while True:
#         if all(n % div == 0 for div in dividers[::-1]):
#             return n
#         n += 2

def smallest_multiple_3(multiple_limit):
    prime_set = set()
    for num in range(2, multiple_limit+1):
        prime_flag = True
        for val in range(2, num):
            if num % val == 0:
                prime_flag = False
                break
        if prime_flag:
            prime_set.add(num)
    result = 1
    for num in prime_set:
        result_mult = 1
        for exp_num in range(1, multiple_limit):
            if num ** exp_num <= multiple_limit:
                result_mult = num ** exp_num
            else:
                break
        result *= result_mult
    return result




if __name__ == "__main__":
    start_time = time.perf_counter()
    print(smallest_multiple_3(20))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Программа выполнилась за {elapsed_time:.6f} секунд")