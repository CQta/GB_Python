from random import randint


def input_kol(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


fl_bot = bool(int(input("Введите 0 что бы играть вдвоём")))
print(fl_bot)
player1 = input("Введите первого игрока: ")
player2 = "BOT" if fl_bot else input("Введите второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while value > 28:
    if flag:
        k = input_kol(player1)
        value -= k
        flag = False
    else:
        print("Ход бота")
        k = randint(1, 28) if fl_bot else input_kol(player2)
        value -= k
        flag = True
    print(f"Осталось {value} конфет")
if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
