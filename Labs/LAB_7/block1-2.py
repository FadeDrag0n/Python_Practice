# Блок 1. Робота з файловою системою та форматом JSON
import json
import math

#1.1 Запис у текстові файли:
print('#Блок 1. Робота з файловою системою та форматом JSON\n')
f = open('first.txt', 'w')
f.write('Python\n')
f.write('html\n')
write_list = ['Python\n', 'MySQL\n', 'MyJavaScript\n', 'Dota 2\n']
f.writelines(write_list)
f.close()

#1.2. Читання даних:

f2 = open('first.txt', 'r')
print(f2.read())
f2.close()

f2 = open('first.txt', 'r')
print(f2.readline())
f2.close()

f2 = open('first.txt', 'r')
print(f2.readlines())
f2.close()

with open('first.txt') as f:
    for line in f:
        print(line, end='')

# 1.3. Серіалізація JSON:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
with open('test.json', 'w') as file:
    json.dump(dict1, file, indent=4)

dict2 = {'g': 14, 'z': 21, 'o': 311, 'x': 41}
json_str = json.dumps(dict2)
print(json_str)
with open('test2.json', 'w') as file:
    file.write(json_str)
with open('test.json','r') as file:
    dict_json=json.load(file)
dict3 = {value: key for (key, value) in dict_json.items()}
print(dict3)

#Блок 2. Проектування функцій та передача параметрів

#2.1. Базові функції та механізми типізації:

print('\n#Блок 2. Проектування функцій та передача параметрів\n')

def max_value(value1, value2):
    return max(value1, value2)

print(max_value(1, 2), type(max_value(1, 2)))
print(max_value(1.5, 3), type(max_value(1.5, 3)))
print(max_value(1.5, 3.2), type(max_value(1.5, 3.2)))

#  2.2. Маніпуляція даними:

def swap_value(value1, value2):
    return value2, value1

a, b = (5, 4)
print(a, b)
a, b = swap_value(a, b)
print(a, b)

def double_list(list_):
    return [item * 2 for item in list_]

list1 = [1, 2, 3, 4, 5, 6]
list2 = double_list(list1)
print(list1)
print(list2)

def remove_first_letter(str_):
    word_list = str_.split()
    removed_list = []
    for item in word_list:
        removed_list.append(item[1:])
    return ' '.join(removed_list)

print(remove_first_letter('Hello world my name is Artem'))

#  2.3. Алгоритмічні задачі:

def number_sum(num1):
    return sum(int(digit) for digit in str(abs(num1)))

def number_mul(num1):
    return math.prod(int(digit) for digit in str(abs(num1)))

print(number_sum(-51433))
print(number_mul(54323))

def moda_of_list(*list_):
    return max(list_, key=list_.count)
print(moda_of_list(1, 2, 2, 4, 4, 3, 4))
#  2.4. Області видимості та анотації:

global_counter = 0

def practice_function(str_: str) -> int:
    global global_counter
    global_counter += 1
    outer_value = 10
    print(f'global_counter = {global_counter}')

    def update_inner_value():
        nonlocal outer_value
        outer_value += 5

    update_inner_value()
    print(f'outer_value = {outer_value}')
    return int(str_)

print(practice_function('15') + 25)