#Перевантаження операторів (Магічні методи) Наділіть ваші об'єкти здатністю взаємодіяти через стандартні символи Python:

class Salaries:
    __slots__ = ('name', 'amount')
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __iadd__(self, other):
        if isinstance(other, Salaries):
            self.amount += other.amount
        else:
            self.amount += other
        return self

    def __eq__(self, other):
        if not isinstance(other, Salaries):
            return NotImplemented
        return self.amount == other.amount

    def __call__(self, value1):
        return self.amount + value1

    def __getitem__(self, item):
        arr = [self.name, self.amount]
        return arr[item]

    def __repr__(self):
        return f'Salaries({self.name=}, {self.amount=})'


sal1 = Salaries("Ann", 67)
sal2 = Salaries("Kate", 67)

print(sal1 + sal2)
sal1 += 100
print(sal1.amount)
sal1.amount = 67
print(sal1 == sal2)
print(sal1 is sal2)
value = sal1(500)
print(value)

print(sal1[1])
print(sal2[0])
print(sal1)

#sal1.hello = 5 AttributeError: 'Salaries' object has no attribute 'hello' and no __dict__ for setting new attributes

for_eval = "print(sal1)"
eval(for_eval)

