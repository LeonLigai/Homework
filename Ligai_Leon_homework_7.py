while True:


    try:

        number = int(input('Введите трехзначное число: '))




        if (-100 >= number >= -999) or (100 < number < 1000):

            if number >= 0:

                first = number // 100

                third = number % 10

                second = str(number)

                print(f'Ваше число: {number}\n'

                  f'Наоборот: {third}{second[1]}{first}\n')




                if first == third:

                    print(f'Это палиндром? {True}\n'

                          f'Схема проверки: {number} = {third}{second[1]}{first}\n')

                elif first != third:

                    print(f'Это палиндром? {False}\n'

                    f'Схема проверки -> {number} != {third}{second[1]}{first}\n')

            elif number < 0:

                print('Все числа с минусовым значением заведомо считаются не универсальными')

            else:

                break

        else:

            print('Вводите только трехзначные числа\n')





    except Exception:

        print('Вводите только трехзначные числа!')

