# Реалізуй клас NightWatch (Нічна Варта) для управління братами ордена. Він повинен:
# - Зберігати список братів і їх звання (ranger, steward, builder)
# - Мати метод recruit(name, rank) для зарахування
# - Мати метод deserters() що повертає список дезертирів (тих, кого видалили)
# - Мати метод count_by_rank() що повертає dict зі статистикою по рангам
from collections import Counter

class NightWatch:

    def __init__(self):
        self.recruit_list = []
        self.deserter_list = []

    def recruit(self, name, rank):
        self.recruit_list.append((name, rank))

    def remove(self, name):
        for recruit in self.recruit_list:
            if recruit[0] == name:
                self.deserter_list.append(recruit[0])
                self.recruit_list.remove(recruit)
                break

    def count_by_rank(self):
        return dict(Counter(rank for _ , rank in self.recruit_list))

    def deserters(self):
        return self.deserter_list

    def __str__(self):
        recruits = self.recruit_list if self.recruit_list else "No recruits"
        deserters = self.deserter_list if self.deserter_list else "No deserters"
        return f"Recruits: {recruits}\nDeserters: {deserters}"





watch = NightWatch()
watch.recruit("Jon Snow", "ranger")
watch.recruit("Sam Tarly", "steward")
watch.recruit("Sir Alice", "ranger")
watch.recruit("Pyp", "steward")
watch.remove("Pyp")  # дезертир

print(watch)



print(watch.count_by_rank())

print(watch.deserters())
