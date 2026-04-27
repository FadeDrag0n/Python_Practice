#БЛОК 1

input1 = float(input('Input number 1: '))
input2 = float(input('Input number 2: '))

class SixSevenException(Exception):
    pass

try:
    if input1 == 67 or input2 == 67:
        raise SixSevenException("Number 67 is forbidden")
    res = input1 / input2
except ZeroDivisionError:
    print(ZeroDivisionError.__name__)
except SixSevenException as e:
    print(e)
else:
    print('Result:', res)
finally:
    print('Finally!')
