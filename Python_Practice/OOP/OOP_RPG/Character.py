"""A class pack for a console mini RPG response for Character class and additional descendant classes"""
from random import randint
import Equipment

class Character:
    _count = 0

    def __init__(self, name: str = None, max_hp: int = 100, defence: int = 5, dmg: int = 15, armor: Equipment.Armor = None, weapon: Equipment.Weapon = None):
        Character._count += 1
        self.name = name if name else f"New_Player_{Character._count}"
        self.lvl = 1
        self.max_hp = max_hp
        self.defence = defence
        self.dmg = dmg
        self.armor = armor if armor else Equipment.Armor('No Armor')
        self.weapon = weapon if weapon else Equipment.Weapon('No Weapon')
        self.evasion = 0
        self.dmg_mul_attacks = (1, 0)
        self.heal = 0

        self.strength = max_hp
        self.agility = defence
        self.intelligence = dmg


    def level_up(self):
        self.lvl += 1
        self.max_hp = round((self.lvl*self.strength*0.5)) + self.strength
        self.defence = round((self.lvl*self.agility*0.5)) + self.agility
        self.dmg = round((self.lvl*self.intelligence*0.5)) + self.intelligence
        print(f'{self.name} reached lvl {self.lvl}!')
        print(self)

    def level_ups(self, value):
        for i in range(value):
            self.level_up()

    def fight(self, enemy):
        print(f'{self.name} started fight with: {enemy.name}!\n')
        print(f'{self}\n{self.armor}\n{self.weapon}\n')
        print(f'{enemy}\n{enemy.armor}\n{enemy.weapon}\n')
        self_hp = self.max_hp + self.armor.bonus_health
        enemy_hp = enemy.max_hp + enemy.armor.bonus_health
        print('\nBattle Log:\n\n')
        self.ability_on()
        enemy.ability_on()
        print('\n')
        while True:
            if self.dmg_mul_attacks[1] > 1:
                print(f'{self.name} next attack will get x{self.dmg_mul_attacks[0]} damage multiplier')
                self_mul = self.dmg_mul_attacks[0]
                self.dmg_mul_attacks = (self.dmg_mul_attacks[0], enemy.dmg_mul_attacks[1]-1)
            else: self_mul = 1
            if enemy.dmg_mul_attacks[1] > 1:
                print(f'{enemy.name} next attack will get x{enemy.dmg_mul_attacks[0]} damage multiplier')
                enemy_mul = enemy.dmg_mul_attacks[0]
                enemy.dmg_mul_attacks = (enemy.dmg_mul_attacks[0], enemy.dmg_mul_attacks[1]-1)
            else: enemy_mul = 1
            self_evaded = 0 if randint(1, 100) < self.evasion else 1
            enemy_evaded = 0 if randint(1, 100) < enemy.evasion else 1
            hit = (randint(self.dmg*7, self.dmg*13)/10)
            enemy_hit = (randint(enemy.dmg*7, enemy.dmg*13)/10)

            self_received_dmg = round(max(0, round(enemy_hit - self.defence + enemy.weapon.bonus_damage - self.armor.bonus_defense) * self_evaded * enemy_mul))
            enemy_received_dmg = round(max(0, round(hit - enemy.defence + self.weapon.bonus_damage - enemy.armor.bonus_defense) * enemy_evaded * self_mul))

            self_hp -= self_received_dmg
            enemy_hp -= enemy_received_dmg


            if enemy_received_dmg != 0:
                print(f'{self.name} dealt {hit} + {self.weapon.bonus_damage} damage. {enemy.name} received {enemy_received_dmg} through {enemy.defence} + {enemy.armor.bonus_defense} defence. {enemy.name} hp: {enemy_hp + enemy_received_dmg} - {enemy_received_dmg} = {enemy_hp}')
            elif not enemy_evaded:
                print(f'{self.name} dealt {hit} + {self.weapon.bonus_damage} damage. {enemy.name} evaded with {enemy.evasion}%!. {enemy.name} hp: {enemy_hp}')
            else:
                print(f'{self.name} dealt {hit} + {self.weapon.bonus_damage} damage. {enemy.name} blocked all damage with {enemy.defence} + {enemy.armor.bonus_defense} defence. {enemy.name} hp: {enemy_hp}')
            if self_received_dmg != 0:
                print(f'{enemy.name} dealt {enemy_hit} + {enemy.weapon.bonus_damage} damage. {self.name} received {self_received_dmg} through {self.defence} + {self.armor.bonus_defense} defence. {self.name} hp: {self_hp + self_received_dmg} - {self_received_dmg} = {self_hp}')
            elif not self_evaded:
                print(f'{enemy.name} dealt {enemy_hit} + {enemy.weapon.bonus_damage} damage. {self.name} evaded with {self.evasion}%!. {self.name} hp: {self_hp}')
            else:
                print(f'{enemy.name} dealt {enemy_hit} + {enemy.weapon.bonus_damage} damage. {self.name} blocked all damage with {self.defence} + {self.armor.bonus_defense} defence. {self.name} hp: {self_hp}')

            if self.heal != 0 and self_hp > 0:
                self_hp += self.heal
                print(f'{self.name} healed! +{self.heal}hp! Current hp: {self_hp}')
            if enemy.heal != 0 and enemy_hp > 0:
                enemy_hp += enemy.heal
                print(f'{enemy.name} healed! +{enemy.heal}hp! Current hp: {enemy_hp}')

            print('\n\n')

            if (self_hp <= 0) and (enemy_hp <= 0):
                print(f'{self.name} ended fight with {enemy.name} Tie!')
                self.ability_off()
                enemy.ability_off()
                break
            if enemy_hp <= 0:
                print(f'{self.name} win fight!')
                self.ability_off()
                enemy.ability_off()
                self.level_up()
                break
            if self_hp <= 0:
                print(f'{enemy.name} win fight!')
                self.ability_off()
                enemy.ability_off()
                enemy.level_up()
                break

    def equip_wooden(self):
        self.armor = Equipment.wooden_armor
        self.weapon = Equipment.wooden_sword

    def equip_bronze(self):
        self.armor = Equipment.bronze_armor
        self.weapon = Equipment.bronze_sword

    def unequip(self):
        self.armor = Equipment.no_armor
        self.weapon = Equipment.no_sword

    def ability_on(self):
        print(f'{self.name} has no ability!')

    def ability_off(self):
        ...

    def __str__(self):
        return f"{self.name} lvl - {self.lvl} hp - {self.max_hp} defence - {self.defence} dmg - {self.dmg}"