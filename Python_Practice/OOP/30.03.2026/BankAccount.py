class Validated:
    def __init__(self, type_, min_val=None, max_val=None):
        self.type_ = type_
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, obj_type=None):
        if obj is None:          # якщо звертаємось через клас, а не екземпляр
            return self          # повертаємо сам дескриптор
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.type_):
            raise TypeError(f"'{self.name}' must be of type {self.type_.__name__}, got {type(value).__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"'{self.name}' cannot be less than {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"'{self.name}' cannot be greater than {self.max_val}")
        obj.__dict__[self.name] = value


class BankAccount:
    owner = Validated(type_=str)
    balance = Validated(type_=float, min_val=0.0)

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self) -> str:
        return f"Owner: {self.owner}, Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"


# --- Тест ---
account = BankAccount("Artem", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(9000.0)
print(account)

# --- Перевірка помилок ---
try:
    account.balance = -100.0       # ValueError
except ValueError as e:
    print(f"ValueError: {e}")

try:
    account.owner = 123            # TypeError
except TypeError as e:
    print(f"TypeError: {e}")

try:
    bad = BankAccount("Bob", -50.0)  # ValueError одразу при створенні
except ValueError as e:
    print(f"ValueError: {e}")
