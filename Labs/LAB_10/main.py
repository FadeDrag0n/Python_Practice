#  Варіант 14:
#                     Об'єкти – місця веселого відпочинку молоді ( клуби, бари...). Поля (атрибути):
# Тип об’єкту відпочинку
# Кількість місць
# Кількість робочих годин


class Rest:
    age = 50

    def __init__(self, categories = None, places = 10, hours = 12):
        self.__categories = categories or []
        self.__hours = hours
        self.__places = places

    def get_categories(self):
        return self.__categories

    def set_categories(self, categories):
        self.__categories = categories

    def get_hours(self):
        return self.__hours

    def set_hours(self, hours):
        self.__hours = hours

    def del_hours(self):
        del self.__hours

    hours = property(get_hours, set_hours, del_hours)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, places):
        if not isinstance(places, int):
            raise ValueError("places must be an integer")
        self.__places = places

    def __str__(self):
        str_categories = ", ".join(map(str, self.__categories))
        return f'Rest categories: {str_categories} | places: {self.__places} | hours: {self.__hours}'


rest1 = Rest(['bar', 'disco', 'party'], 200, 8)
print(rest1.get_categories())
rest1.set_categories(['bar1', 'disco2', 'party3'])
print(rest1.get_categories())

rest1.hours = 50
print(rest1)

rest1.places = 150
print(rest1)

#pitfall

#print(rest1.__places) # 'Rest' object has no attribute '__places'
rest1.__places = 500
print(rest1.__places)
print(rest1)

