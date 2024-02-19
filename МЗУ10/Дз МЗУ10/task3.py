name_student = {
    'Анна',
    'Виктория',
    'Ника',
    'Владимир',
    'Иван',
    'Дарья',
    'Ирина'
}

while True:
    input_name_student = input("Введите имя ученика -> ")

    if input_name_student.lower() == 'стоп':
        break

    name_student.remove(input_name_student)

print(list(name_student))
