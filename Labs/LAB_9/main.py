#  Варіант 14:
#                     Об'єкти – місця веселого відпочинку молоді ( клуби, бари...). Поля (атрибути):
# Тип об’єкту відпочинку
# Кількість місць
# Кількість робочих годин


class Rest:
    age = 50

    def __init__(self, categories = None, places = 10, hours = 12):
        self.categories = categories or []
        self.places = places
        self.hours = hours

    @staticmethod
    def return_tip(order_price: float) -> float:
        return order_price * 0.1

    @classmethod
    def from_string(cls, categories, data: str):
        places, hours = data.split(",")
        return cls(categories, int(places), int(hours))

    def __str__(self):
        str_categories = ", ".join(map(str, self.categories))
        return f'Rest categories: {str_categories} | places: {self.places} | hours: {self.hours}'


class SingletonExm:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name



rest1 = Rest(['bar', 'disco', 'party'], 200, 8)
rest2 = Rest()
print(rest1.categories)
print(rest2.categories)

#3. Динамічні атрибути:

rest2.open = True
print(rest2.open)
# print(rest1.open) # AttributeError!

#4. Статичні дані (Атрибути класу):

print(Rest.age) # 50
print(rest1.age)
print(rest2.age) # 50

Rest.age = 75
rest1.age = 100

print(Rest.age)
print(rest1.age)
print(rest2.age)


#5. Типологія методів:

print(Rest.return_tip(500))
print(rest2.return_tip(1500))
rest3 = Rest.from_string(['bar'], '500,24')

#6. Рядкове представлення:

print(rest3)
print(rest1)

#7. Управління створенням (__new__):

single1 = SingletonExm('1')
single2 = SingletonExm('2')

print(single1)
print(single2)