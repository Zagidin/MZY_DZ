user_1, user_2 = (
    input("Введите целые числа(user_1): "),
    input("Введите целые числа(user_2): ")
)

users_number = []

for interesting in user_1.split():
    users_number.append(int(interesting))

for interesting in user_2.split():
    users_number.append(int(interesting))

element_count = {}
for element in users_number:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

unique_elements = [element for element, count in element_count.items() if count != 1]
unique_elements.sort()

print(unique_elements)
