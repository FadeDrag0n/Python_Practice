def sum_of_divisors(n):
    sum_ = 0
    for number in range(1, n):
        if number % 3 == 0 or number % 5 == 0:
            sum_ += number
    return sum_

def sum_of_divisors_2(n, k):
    m = (n-1) // k
    return k * m * (m + 1) // 2

def main():
    print(sum_of_divisors(1000))
    print(sum_of_divisors_2(1000, 3) + sum_of_divisors_2(1000, 5) - sum_of_divisors_2(1000, 15))

if __name__ == "__main__":
    main()