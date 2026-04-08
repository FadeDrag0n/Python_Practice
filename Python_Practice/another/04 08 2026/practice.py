import math
from collections import Counter

# Найди сумму только чётных чисел в списке
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(sum(i for i in numbers if i % 2 == 0))
# Ожидаемый ответ: 20

text = "hello world python"

print(' '.join(word[::-1] for word in text.split()))


# Подсчитай, сколько раз встречается каждая буква
word = "banana"
print(Counter(word))

# Ожидаемый результат: {'b': 1, 'a': 3, 'n': 2}


def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(2, int(math.sqrt(n)) + 2, 2):
        if n % i == 0:
            return False
    return True



# Напиши функцию, которая проверяет, является ли число простым
print(is_prime(7)) # True
print(is_prime(10)) # False
print(is_prime(97))

lines = 0
words = 0
with open('.txt', 'r') as f:
    for line in f:
        lines += 1
        words += len(line.split())
print('lines: ', lines)
print('words: ', words)

# Прочитай файл, посчитай количество строк и слов
# Выведи: "Строк: X, Слов: Y"