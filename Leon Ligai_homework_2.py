sock = ("wrtpsdfghjklzxcvbnmqцкнгшщзхфвпрлджчстбьъ")
sock2 = ("aeiouйуеыаоэяию")


while True:
    a = input("Введите ваше слово:").lower()
    sogl = 0
    gl = 0
    if a == "q":
        print("Выход из программы.")
        break
    for i in a:
        for s in sock:
            if i == s:
                sogl += 1
        for d in sock2:
            if i == d:
                gl += 1
    b = len(a)
    c = sogl / b * 100
    c = round(c, 2)
    d = gl / b * 100
    d = round(d, 2)

    print(f'Слово: {a}\n',
        f'Количество букв: {b}\n',
          f'Согласных букв: {sogl}\n',
          f'Гласных букв: {gl}\n',
          f'Гласные/Согласные:{d}% / {c}%\n')

