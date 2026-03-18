class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant : {self.restaurant_name} opens with {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class User:

    def __init__(self, first_name, last_name, login, password, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} {self.login} {self.password}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = flavor

    def get_flavor(self):
        print(self.flavor)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Privileges:", ", ".join(self.privileges))

class Admin(User):

    def __init__(self, first_name, last_name, login, password, privileges):
        super().__init__(first_name, last_name, login, password)
        self.privileges = Privileges(privileges)


restaurant1 = Restaurant('William place', 'Japanese')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('Wild Savanna', 'Mexican')
restaurant3 = Restaurant('Krutuy Kozak', 'Ukrainian')
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
user1 = User('admin', 'admin', 'admin', '19-2340gtquweap')
user2 = User('Natan', 'Drake', 'Natan', '45vcyt457u345312ty')
user1.describe_user()
user1.greet_user()
user2.greet_user()
user2.describe_user()

#9.4
restaurant4 = Restaurant('Russian Classic', 'Russian')
print(restaurant4.number_served)
restaurant4.number_served = 15
print(restaurant4.number_served)
restaurant4.set_number_served(150)
print(restaurant4.number_served)
restaurant4.increment_number_served(20)
print(restaurant4.number_served)

#9.5
user3 = User('admin', 'admin', 'admin', '19-2340gtquweap')
print(user3.login_attempts)
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)

#9.6 - 9.8

icecream1 = IceCreamStand('Ice Cream', 'ice cream', 'Chocolate')
icecream1.get_flavor()

admin1 = Admin('Olga', 'Polovyk', 'admin', '425332345524451', ['Can remove users', 'Can create orders'])
admin1.privileges.show_privileges()