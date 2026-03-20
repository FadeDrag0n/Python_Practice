def find_all_numbers(value: int, lim: int):
    for i in range(value, lim + 1):
        if str(value) in str(i):
            yield i

if __name__ == '__main__':
    v = int(input('Input a number: '))
    l = int(input('Input a limit: '))
    leng = 0
    gen = find_all_numbers(v, l)
    with open(f'find_{v}_in_{l}.txt', 'w') as f:
        for n in gen:
            f.write(f'{str(n)} ')
            leng += 1
    print(f'{leng} elements added to find_{v}_in_{l}.txt')