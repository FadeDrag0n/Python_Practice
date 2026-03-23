# 1. Робота з анонімними функціями та вбудованими методами
from functools import reduce

#1.1

list_ = [[1, 8], [5, 3], [2, 6]]
print(sorted(list_, key = lambda i: i[1]))

#1.2

ids = ['id1', 'id2', 'id30', 'id3', 'id100', 'id22']
print(sorted(ids, key = lambda i: int(i[2:])))

# 1.3
list2_ = ['cat', 'dog', 'cow']
print(list(map(lambda i: i.upper(), list2_)))

#1.4
print(list(filter(lambda i: 'o' in i, list2_)))

#2. Сортування словників

dict_ = {'a': 4, 'b': 5, 'c': 2, 'd': 1}
dict2 = sorted(dict_.items(), key = lambda i: i[1])
print(dict2)

#3. Масштабування даних

list3_ = [1, 2, 3, 10, 25]
list_mul_2_1 = [value*2 for value in list3_]
list_mul_2_2 = list(map(lambda x: x*2, list3_))
print(list_mul_2_1, list_mul_2_2)

#4. Обробка чисел

def count_total(val) -> int:
    values = list(int(item) for item in str(val) if item.isdigit())
    return sum(values)

value = 123.4
print(count_total(value))

#5. Агрегація даних у кортежах

tuple_ = ((2, 3), (1, 2))
print(sum(sum(tuple_, tuple())))
print((sum(sum(item) for item in tuple_)))

#6. Однорядковий ввід даних

input_value = input('Enter a numbers divided by spaces: ')
value_list = input_value.split(' ')
value_list_int = list(map(int, value_list))
print(value_list_int)

#7. Поелементне піднесення до степеня

list1 = [2, 3, 4, 1]
list2 = [0, 3, 2, 1]
#list3 =list(item ** list2[index] for index, item in enumerate(list1))
list3 = list(map(lambda x: x[0] ** x[1], zip(list1, list2)))
print(list3)

#8. Паралельна ітерація (використання zip) )

key_list = ['a', 'b', 'c', 'd']
value_list = [0, 3, 2, 1]
dict3 = dict(zip(key_list, value_list))
print(dict3)

#9. Визначення розрядності числа
def find_len(val):
    return reduce(lambda x, _: x + 1, str(val), 0)

print(find_len(1544440))
