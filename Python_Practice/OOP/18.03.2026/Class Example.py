class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cousin_type = cuisine_type
    def describe_restaurant(self):
        print(f'Restaurant : {self.restaurant_name} opens with {self.cousin_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')

class User:
    def __init__(self, first_name, last_name, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} {self.login} {self.password}')
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

restaurant1 = Restaurant('William place', 'Japanese')
print(restaurant1.restaurant_name)
print(restaurant1.cousin_type)
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