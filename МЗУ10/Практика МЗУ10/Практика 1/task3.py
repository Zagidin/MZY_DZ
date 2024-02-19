numbers = input("Введи элементы списка через запятую и пробел --> ")

numbers = [int(num) for num in numbers.split(', ')]

# numbers = sorted(numbers)
print(list(set(numbers)))
