from math import sqrt


def find_pifagor(num):
    for a in range(1, num):
        for b in range(1, num):
            c = num - a - b
            if c > 0 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                return a * b * c
    return None



print(find_pifagor(1000))