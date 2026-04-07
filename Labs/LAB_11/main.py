#1. Основи наслідування та ієрархія

class Vehicle:
    def __init__(self, name, model, year):
        print('Vehicle init called.')
        self.name = name
        self._model = model
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

class Car(Vehicle):
    def __init__(self, name, model, year, make):
        print('Car init called.')
        super().__init__(name, model, year)
        self.make = make

class Truck(Car):
    def __init__(self, name, model, year, make, length):
        print('Truck init called.')
        Car.__init__(self, name, model, year, make)
        self.length = length

    def __str__(self):
        return f'{self.name=}, {self._model=}, {self.year=}, {self.make=}, {self.length=}'


def length_sum(collection1):
    return sum(item.length for item in collection1)


truck1 = Truck('Truck 1', 100, 200, 'BM', 500)
truck2 = Truck('Truck 2', 100, 200, 'BM', 300)
truck3 = Truck('Truck 3', 100, 200, 'BM', 100)
truck4 = Truck('Truck 4', 100, 200, 'BM', 150)

truck_list = [truck1, truck2, truck3, truck4]
print(length_sum(truck_list))