#2. Абстракція та інтерфейси
from abc import ABC, abstractmethod


class CoolNumbers(ABC):
    def __init__(self, cool_value):
        self.cool_value = cool_value

    @abstractmethod
    def print_cool(self):
        pass


class SixSeven(CoolNumbers):
    def __init__(self, cool_value):
        super().__init__(cool_value)
        self.is_six_seven = True

    def print_cool(self):
        print(self.cool_value)


class WildPython:
    def __init__(self, cool_value):
        self.cool_value = cool_value

    def print_cool(self):
        print(self.cool_value)



six_seven = SixSeven(500)
six_seven2 = SixSeven(1500)
wild1 = WildPython(100)

cool_list = [six_seven, six_seven2, wild1]
print(max(item.cool_value for item in cool_list))

six_seven.print_cool()