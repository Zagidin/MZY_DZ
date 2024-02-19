input_text = input("Введите текст -->")

if len(input_text) == len(set(input_text)):
    print("Все символы уникальные")
else:
    print("Нет")
