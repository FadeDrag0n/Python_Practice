#4. Множинне наслідування та MRO

class A:
    def __init__(self, value):
        super().__init__(value)

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


#Відносини між класами:

class Page:
    def __init__(self, content):
        self.content = content

    def __del__(self):
        print(f"Page '{self.content}' deleted.")

class Book:
    def __init__(self, title):
        self.title = title
        self.pages = [Page("Task 1"), Page("Task 2")]

    def __del__(self):
        print(f"Book '{self.title}' deleted.")

my_book = Book("Python 101")
print(my_book.title)
del my_book

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Employee '{self.name}' deleted.")


class Work:
    def __init__(self, employee):
        self.employee = employee

    def __del__(self):
        print(f"Work with employee: '{self.employee.name}' deleted.")

emp1= Employee("Марія", 6)

work1 = Work(emp1)
del work1

input()