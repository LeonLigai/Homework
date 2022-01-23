country = {
'kg' : {'red' , 'yellow'} ,
'kz': {'yellow' , 'blue'} ,
'it': {'green', 'white', 'red'} ,
'de': {'black', 'red' ,'yellow'},
'ru': {'white', 'blue', 'red'}
}

while True:
    user = input('Введите цвет: ')
    caunt = []
    if user == "q":
        print('Выход из программы.')
        break
    for name,colours in country.items():
            if set(user.split()).issubset(colours):
                print(name)
                caunt.append(colours)
    if len(caunt) < 1:
        print('такого нету в списке')












