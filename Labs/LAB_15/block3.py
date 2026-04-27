#Блок 3. Спеціалізовані колекції (Module collections)
from collections import Counter, defaultdict

#3.1. Підрахунок елементів: Використовуючи Counter, проаналізуйте список [1, 2, 3, 1, 1, 2] і виведіть статистику частоти вкладень.

list1 = [1, 2, 3, 1, 1, 2]
print(Counter(list1))

#3.2. Словники з типізацією: Створіть об'єкт defaultdict, де значеннями за замовчуванням є списки, та наповніть його даними згідно з прикладом: {1: ['one1', 'one2'], 2: ['two', 'two']}.

ddict = defaultdict(list)
print(dict(ddict))

ddict[1].append('one1')
ddict[1].append('one2')

ddict[2].append('two')
ddict[2].append('two')
print(dict(ddict))