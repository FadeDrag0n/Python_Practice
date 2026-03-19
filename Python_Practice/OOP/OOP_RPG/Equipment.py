"""A class pack for a console mini RPG responsible for armor and weapons"""
class Armor:
    def __init__(self, name, bonus_health = 0, bonus_defense = 0):
        self.name = name
        self.bonus_health = bonus_health
        self.bonus_defense = bonus_defense

    def __str__(self):
        return f'Armor name: {self.name} | Bonus health: {self.bonus_health} | Bonus defense: {self.bonus_defense}'

class Weapon:
    def __init__(self, name, bonus_damage = 0):
        self.name = name
        self.bonus_damage = bonus_damage

    def __str__(self):
        return f'Weapon name: {self.name} | Bonus damage: {self.bonus_damage}'

no_armor = Armor('No Armor')
no_sword = Weapon('No Sword')
wooden_armor = Armor('Wooden Armor', 25, 2)
bronze_armor = Armor('Bronze Armor', 50, 5)
wooden_sword = Weapon('Wooden Sword', 10)
bronze_sword = Weapon('Bronze Sword', 25)