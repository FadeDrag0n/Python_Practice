#БЛОК 2
import numpy as np

#2.1. Створення масивів:
print("2.1. Створення масивів:\n")
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

array1 = np.array(list1)
array2 = np.array(tuple1)
array3 = np.arange(3000)

print(array1)
print(array2)
print(array3)

#2.2. Арифметичні операції: Знайдіть суму та добуток створених масивів. Помножте всі елементи результату на 3.
print("\n2.2. Арифметичні операції: Знайдіть суму та добуток створених масивів. Помножте всі елементи результату на 3.\n")

array_sum = array1 + array2
array_multi = array1 * array2
array_multi_by_3 = array3 * 3

print(array_sum)
print(array_multi)
print(array_multi_by_3)

#2.3. Візуалізація та розмірність:
print("\n2.3. Візуалізація та розмірність:\n")

print(array_multi_by_3)
np.set_printoptions(threshold=3000)
print(array_multi_by_3)

print(array_multi_by_3.size)
print(array_multi_by_3.shape[0])
#print(array_multi_by_3.shape[1])
print(array_multi_by_3.ndim)

array4 = np.zeros((5, 5))
array4[1:4, 2:5] = 7

print(array4)

arr5 = np.array([1, 2, 3, 4, 5])

view_arr = arr5.view()
copy_arr = arr5.copy()

arr5[0] = 100

print("Original:", arr5)
print("View:", view_arr)
print("Copy:", copy_arr)