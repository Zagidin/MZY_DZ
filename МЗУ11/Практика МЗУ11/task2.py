sl1, sl2 = (
    input("Введите 1-ую строку: "),
    input("Введите 2-ую строку: ")
)

sl1, sl2 = (
    set(sl1),
    set(sl2)
)

print(len(sl1-sl2))
