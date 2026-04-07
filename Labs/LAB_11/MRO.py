#4. Множинне наслідування та MRO

class A:
    def __init__(self, value):
        self.value = value

class A1:
    def __init__(self, value):
        super().__init__(value)

class B(A):
    def __init__(self, value):
        super().__init__(value)

class B1(A1):
    def __init__(self, value):
        super().__init__(value)

class B2(B, B1):
    def __init__(self, value):
        super().__init__(value)

class C(A):
    def __init__(self, value):
        super().__init__(value)

class C1(A):
    def __init__(self, value):
        super().__init__(value)

class D(C, C1):
    def __init__(self, value):
        super().__init__(value)


print(D.__mro__)
print(B2.__mro__)