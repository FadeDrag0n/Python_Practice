def even_fibonacci_sum(n):
    num = 1
    prev_num = 0
    fib_list = []
    while num < n:
        fib_list.append(num)
        num, prev_num = num + prev_num, num
    return sum(num for num in fib_list if num % 2 == 0)

def optimized_fibonacci_sum(n):
    num, next_num = 1, 2
    total = 0
    while num < n:
        if num % 2 == 0:
            total += num
        num, next_num = next_num, num + next_num
    return total



def main():
    print(f'sum of elements: {even_fibonacci_sum(4000000)}')
    print(f'sum of elements: {optimized_fibonacci_sum(4000000)}')

if __name__ == "__main__":
    main()