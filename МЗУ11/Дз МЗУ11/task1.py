user_1, user_2 = (
    input("Введите свои интересы(user_1): "),
    input("Теперь введите ваши интересы(user_2): ")
)

users_list = []

for interesting in user_1.split():
    users_list.append(interesting)

for interesting in user_2.split():
    users_list.append(interesting)

element_count = {}
for element in users_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

unique_elements = [element for element, count in element_count.items() if count == 1]

print(unique_elements)
