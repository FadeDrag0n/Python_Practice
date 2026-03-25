import math

list1 = [1, 2, 3, 4]
list2 = [0, 1, 2, 3]

print(list(map(lambda x, y: x**y, list1, list2)))