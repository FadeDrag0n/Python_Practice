import math


# ХУЙНЯ ПОЛНАЯ БУДЕТ ВЫПОЛНЯТЬ ЗАДАЧУ МИЛЛИАРДЫ ЛЕТ

# def largest_prime_factor(n):
#     largest = 0
#     for num in range(n, 2, -1):
#         if n % num == 0:
#             prime_flag = True
#             for divisor in range(2, num):
#                 if num % divisor == 0:
#                     prime_flag = False
#                     break
#             if num > largest and prime_flag == True:
#                 largest = num
#     return largest or f'{n} dont have prime factor'

def largest_prime_factor(n):
    largest = None
    d = 2
    while d * d <= n:
        while n % d == 0:
            largest = d
            n //= d
        d += 1
    if n > 1:
        largest = n  # n само является простым
    return largest if largest else f'{n} не имеет простых делителей'

def main():
    n1 = 13195
    n = 600851475143
    print(f'largest prime factor of {n} is - {largest_prime_factor(n)}')

if __name__ == '__main__':
    main()