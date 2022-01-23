movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Spider-Man": {}
}


def movie_add(movie):
    if movie in movies.keys():
        print("Фильм успешно добавлен")
    else:
        movies.update({movie:dict()})

def atributes():
    for name, rates in movies.items():
        print(f"\nФильм:{name}")
        if len(rates) == 0:
            print("Рейтинг ещё не доступен")
        else:
            print("Рейтинг: ")
            for user, rate in rates.items():
                print(f"{user}: {rate}")

def rate_add(movie):
    if movie not in movies.keys():
        print("Такого фильма не существует")
    else:
        name = input("Введите своё имя:")
        rate = int(input("Введите рейтинг:"))
        if rate < 0 or rate > 10:
            print("Введите оценку от 0 до 10!")
        else:
            movies[movie].update({name: rate})
            print(f"{name} оценено в {rate}")

def rating():
    for movie, rate in movies.items():
        rates = []
        for i in rate.values():
            rates.append(i)
        if len(rates) == 0:
            print(f"Рейтинг ещё не доступен для {movie}")
        else:
            print(f"{movie} рейтинг этого фильма: {sum(rates) / len(rates)}")

while True:
    atributes()
    user = int(input(
        "\nВыберите команду (1 - Добавить фильм, 2 - Добавить оценку к фильму, "
        "3 - Просмотр оценок, 0 - Выход из программы): "
    ))
    if user == 0:
        print("Выход из программы.")
        break
    elif user == 1:
        movie = input("Введите название фильма:")
        movie_add(movie)
    elif user == 2:
        movie = input("Введите название фильма для добавления рейтинга:")
        rate_add(movie)
    elif user == 3:
        rating()
    else:
        print("Данной команды нету.")