play_number = int(input("Введите количество игр: "))

list_play = []

for i in range(1, play_number + 1):
    play = input(f"Введите {i} игру: ")
    list_play.append(play)

print(
    "Принято!"
    if
    len(set(list_play)) == len(list_play)
    else
    "Кто-то из вас ввёл одинаковую игру, Повтор!"
)
