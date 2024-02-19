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
    if 10 < el < 35:
        bag.add(el)
    else:
        continue

print(bag)
