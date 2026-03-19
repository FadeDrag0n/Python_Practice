from random import randint
from random import choice

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self, times):
        res = ', '.join(str(randint(1, self.sides)) for _ in range(times))
        print(f'Result of {times} times: {res}')

if __name__ == "__main__":
    dice1 = Dice()
    dice1.roll_dice(10)
    dice2 = Dice(10)
    dice3 = Dice(20)

    dice2.roll_dice(10)
    dice3.roll_dice(10)

    lottery_pull = ('k', 'i', 'n', 'g', 'c', 'a', 's', 'i', 'n', 'o', 7, 6, 5, 4, 3)
    lottery_prize = 500000
    lottery_ticket_price = 100
    lucky_ticket = [choice(lottery_pull) for _ in range(4)]
    print(lucky_ticket)

    att = 0
    while True:
        att += 1
        my_ticket = [choice(lottery_pull) for _ in range(4)]
        if my_ticket == lucky_ticket:
            profit = lottery_prize - lottery_ticket_price * att
            result = f'+{profit}$' if profit > 0 else f'{profit}$ (in minus)'
            print(f'You won in {att} attempts. Your refund {result}')
            break
