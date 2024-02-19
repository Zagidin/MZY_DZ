user_1, user_2, user_3 = (
    input("Введите любимых авторов(user_1): "),
    input("Введите любимых авторов(user_2): "),
    input("Введите любимых авторов(user_3): ")
)

author_list_user2 = []
author_list = []

for author in user_1.split():
    author_list.append(author)

for author in user_2.split():
    author_list_user2.append(author)

for author in user_3.split():
    author_list.append(author)

unikalnost_author_user_2 = set(author_list_user2) - set(author_list)

print("Авторы, которые любит user_2, но не любят user_1 и user_3: => ", *list(unikalnost_author_user_2))
