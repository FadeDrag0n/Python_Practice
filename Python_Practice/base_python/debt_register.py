def calc_debts(debts_: list) -> tuple:
    total_dict = {}

    for name, amount in debts_:
        if name not in total_dict:
            total_dict[name] = amount
        else:
            total_dict[name] += amount

    return total_dict, max(total_dict, key=lambda n: total_dict[n])



# Очікувана поведінка:
debts = [
    ("Cersei", 500),
    ("Joffrey", 200),
    ("Cersei", 300),
    ("Tyrion", 1000),
]

totals, biggest_debtor = calc_debts(debts)
print(totals)
print(biggest_debtor)
# totals == {"Cersei": 800, "Joffrey": 200, "Tyrion": 1000}
# biggest_debtor == "Tyrion"