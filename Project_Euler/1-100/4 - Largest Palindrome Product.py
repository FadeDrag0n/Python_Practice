import time

# def find_palindrome1(lim):
#     for num in range(lim ** 2, 1, -1):
#         if str(num) == str(num)[::-1]:
#             for factor in range(lim+1, 1, -1):
#                 if num % factor == 0:
#                     factor2 = num // factor
#                     if int(len(str(int(factor2)))) == len(str(lim)):
#                         return num
#     return None
#
# def find_palindrome2(lim):
#     largest = 0
#     for num in range(lim, 99, -1):
#         for num2 in range(lim, 99, -1):
#             if (str(num*num2) == (str(num*num2))[::-1]) and (num*num2 > largest):
#                 largest = num*num2
#     return largest or 'No pair'

def find_palindrome3(lim):
    largest = 0

    for i in range(lim, 100-1, -1):
        if i * i < largest:
            break
        for j in range(i, 100-1, -1):
            num = i*j

            if num <= largest:
                break

            if str(num) == (str(num))[::-1]:
                largest = num
    return largest or 'No pair'


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(find_palindrome3(999))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Программа выполнилась за {elapsed_time:.6f} секунд")