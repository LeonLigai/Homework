import datetime
import random
start = datetime.datetime.now()
number = random.randint(1, 100)
counter = 0
while True:
    try:
        user = int(input("Введите число: "))
        if user < 0 or user > 100:
            print("Вводите цифры только 0-100")
            continue
    except ValueError:
            print("Вводите только цифры!")
    except NameError:
            print('Вводите только цифры!')
    if user == number:
        counter += 1
        end = datetime.datetime.now() - start
        print("Вы ввели правильное число!")
        print(f'Потраченно времни: {end}')
        print(f'Количество попыток: {counter}')
        break
    elif user == number + 5 or user == number - 5:
        print("Очень близко")
        counter += 1
    elif user == number + 10 or user == number - 10:
        print("Близко")
        counter += 1
    elif user > number:
        print("<")
        counter +=1
    elif user < number:
        print(">")
        counter += 1


    print(number)

