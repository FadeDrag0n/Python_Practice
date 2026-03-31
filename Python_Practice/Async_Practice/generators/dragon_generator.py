# У Дейнеріс є дракони: Дрогон, Рейгаль, Вісеріон. Кожен дракон випускає вогонь певною мірою.
# Напиши генератор battle_sequence(dragons, enemies), який:
# - Чергує атаки драконів та ворогів по черзі
# - Пропускає ворогів, якщо їх "здоров'я" <= 0
# - Зупиняється, коли всі вороги переможені
# - Yields рядки у форматі "Drogon attacks Euron (HP remains: 40)"
import itertools


def battle_sequence(dragons, enemies):
    dragon_cycle = itertools.cycle(dragons)
    enemy_names = list(enemies.keys())

    while any(hp > 0 for hp in enemies.values()):
        for enemy in enemy_names:
            if enemies[enemy] <= 0:
                continue

            dragon = next(dragon_cycle)

            enemies[enemy] -= 40
            if enemies[enemy] < 0:
                enemies[enemy] = 0

            yield f"{dragon} attacks {enemy} (HP remains: {enemies[enemy]})"


dr = ["Drogon", "Rhaegal", "Viserion"]
en = {"Euron": 100, "Night King": 200, "Cersei": 50}

for event in battle_sequence(dr, en):
    print(event)