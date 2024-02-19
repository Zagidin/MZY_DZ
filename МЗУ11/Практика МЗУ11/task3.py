hobbies1, hobbies2 = (
    input("Введите ваши интересы(user_1): ").split(),
    input("Введите ваши интересы(user_2): ").split()
)

result1 = set(hobbies1) & set(hobbies2)

result2 = set(hobbies1) | (set(hobbies2))

result = len(result1) / len(result2) * 100

print(round(result))
