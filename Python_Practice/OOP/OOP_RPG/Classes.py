from Character import Character

class Warrior(Character):
    def __init__(self, name=None):
        super().__init__(name, max_hp=180, defence=6, dmg=20)

    def ability_on(self):
        self.heal = self.max_hp / 20
        print(f'{self.name} activated ability! {self.name} will be restore {self.heal} HP each attack')

    def ability_off(self):
        self.heal = 0


class Mage(Character):
    def __init__(self, name=None):
        super().__init__(name, max_hp=60, defence=2, dmg=35)

    def ability_on(self):
        self.dmg_mul_attacks = (round((self.lvl*0.02)+1.5, 1), 4)
        print(f'{self.name} activated ability! {self.name} granted {self.dmg_mul_attacks[0]} damage multiplier for {self.dmg_mul_attacks[1]} attacks')

    def ability_off(self):
        self.dmg_mul_attacks = (1, 0)


class Archer(Character):
    def __init__(self, name=None):
        super().__init__(name, max_hp=100, defence=7, dmg=25)

    def ability_on(self):
        self.evasion = min(45, self.lvl+20)
        print(f'{self.name} activated ability! {self.name} granted {self.evasion}% evasion bonus')

    def ability_off(self):
        self.evasion = 0