# Есть базовый класс Account и два наследника:
# SavingsAccount — начисляет проценты (метод accrue_interest())
# CreditAccount  — позволяет уходить в минус, но до лимита

# Bank агрегирует счета и умеет:
# - add_account(account)
# - transfer(from_id, to_id, amount)
# - total_assets() — сумма всех балансов

# Transaction — отдельный класс, Account хранит их список (композиция)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise Exception("You cannot withdraw less than 500 credits")
        else:
            self.balance -= amount

    def statement(self):
        for transaction in self.transactions:
            print(transaction)



class SavingsAccount(Account):
    def __init__(self, name, balance, rate):
        super().__init__(name, balance)
        self.rate = rate

    def accrue_interest(self):
        self.balance *= self.rate + 1


class CreditAccount(Account):
    def __init__(self, name, balance, limit):
        super().__init__(name, balance)
        self.limit = limit

    def withdraw(self, amount):
        if self.balance - amount < -self.limit:
            print(self.balance - amount)
            raise Exception("You cannot withdraw less than -500 credits")
        else:
            self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_, to_, amount):
        if to_ not in self.accounts or from_ not in self.accounts:
            raise Exception("You cannot transfer money from account that doesn't registered in bank")
        from_.withdraw(amount)
        to_.balance += amount
        from_.transactions.append(Transaction(from_.name, to_.name, amount))
        to_.transactions.append(Transaction(from_.name, to_.name, amount))

    def total_assets(self):
        sum_ = 0
        for account in self.accounts:
            sum_ += account.balance
        return sum_




class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def __str__(self):
        return f"From: {self.from_account}, To: {self.to_account}, Amount: {self.amount}"



bank = Bank()

savings = SavingsAccount("Alice", balance=1000, rate=0.1)
credit  = CreditAccount("Bob", balance=0, limit=500)

bank.add_account(savings)
bank.add_account(credit)

savings.accrue_interest()     # баланс 1100
bank.transfer(savings, credit, 300)
credit.withdraw(100)          # уходит в минус, но в пределах лимита
credit.withdraw(100)          # exceeds limit — исключение!

print(bank.total_assets())           # считает по всем счетам
savings.statement()           # история через Transaction