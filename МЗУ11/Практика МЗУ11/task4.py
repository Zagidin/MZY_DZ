sl1, sl2 = (
    input("Введите первое слово: "),
    input("Введите вторую слово: ")
)

sl1, sl2 = set(sl1), set(sl2)

print(len(sl1 ^ sl2))
