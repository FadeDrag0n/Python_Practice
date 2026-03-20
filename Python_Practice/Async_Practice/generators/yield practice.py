def countdown(n):
    for i in range(n, 0, -1):
        yield i

def cycle(inp_list: list):
    while True:
        for item in inp_list:
            yield item

def only_even(inp_list: list  ):
    for item in inp_list:
        if item % 2 == 0:
            yield item

def flatten(inp_list: list[list]):
    for item in inp_list:
        yield from item

def running_average():
    total, count = 0, 0
    while True:
        value = yield total / count if count else None
        total += value
        count += 1

if __name__ == '__main__':
    #Задание 1

    gen = countdown(5)
    print(next(gen))
    print(next(gen))

    #Задание 2

    list_ = list(countdown(3))
    print(list_)
    gen2 = cycle(list_)
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))

    #Задание 3

    gen = only_even(list(range(52)))
    print(list(gen))

    #Задание 4

    list2 =[[1,2,3],[4,5,6],[7,8,9]]
    gen = flatten(list2)
    print(list(gen))

    #Задание 5

    gen = running_average()
    next(gen)  # инициализация
    print(gen.send(10))  # → 10.0
    print(gen.send(20))  # → 15.0
    print(gen.send(30))  # → 20.0
