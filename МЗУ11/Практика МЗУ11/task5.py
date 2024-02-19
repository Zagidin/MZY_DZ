p1, p2, p3 = (
    set(input("Введите первую строку: ").split()),
    set(input("Введите вторую строку: ").split()),
    set(input("Введите третью строку: ").split())
)

result = (p1 - p2) & (p1 - p3)

print(sorted(result))
