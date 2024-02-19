s = {
    5, 24, -5, 0, 667, -3, -6
}

while True:
    number = int(input("Введите число -> "))

    if number == 0:
        break

    s.add(number)

bag = set()
for el in s:
    if el > 0:
        bag.add(el)
    else:
        continue

bag = sorted(bag, reverse=True)
print(bag)
