s = {
    'школа',
    'парк',
    'теплоход',
    'кинотеатр'
}

name_places = input("Предложите название места отдыха через пробел => ")
for name in name_places.split():
    s.add(name)

print(f"Конечный результат мест отдыха для Выпускного: {list(s)}")
