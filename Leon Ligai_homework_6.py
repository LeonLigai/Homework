ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [2, 4, 6, 8, 10]

kvadrat = list(map(lambda x: x ** 2 , evens))

print(kvadrat)

while True:
    try:
        index = int(input('Введите индекс :'))
        print(ten[index])
    except IndexError:
        print(f'Вводить только числа от 0 до {len(ten) - 1}')
    except ValueError:
        print('Вводить только числа!')
    if index == 'q':
         print('Выход из программы... ')
         break


