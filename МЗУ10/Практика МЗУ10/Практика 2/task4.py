print("\nПривет!\nВыберите одно действие из трёх предложенных => "
      "[<< 1 >> - Добавить, << 2 >> - Удалить, << 3 >> - Выйти]\n")

p = [5, 12, 18, 46, 34, 6]
p_set = set(p)

while True:
    action = input("Введите действие --> ")

    if action == "1":
        element = int(input(f"Введите число, которое хотите добавить в список {list(p_set)} ==> "))
        p_set.add(element)

    elif action == "2":
        element = int(input(f"Введите число, которое хотите удаить из списока {list(p_set)} ==> "))
        if element not in p_set:
            print("Такого числа нету!")
        else:
            p_set.remove(element)

    else:
        print(f"Ваше множество ==> {p_set}")
        break
