numbers = input("Введите числа через пробел ==> ")

bag = set()
for number in numbers.split():
    if int(number) in bag:
        print("Повтор")
    else:
        print("Нет")
        bag.add(int(number))
