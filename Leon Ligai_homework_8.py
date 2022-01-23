import datetime
import time
from random import randint
tries = int(input('Сколько попыток? '))
name = input('Укажите имя: ')
start = datetime.datetime.now()
poputka = tries
while tries != 0:
    a = randint(1, 9)
    b = randint(1, 9)
    c = a * b
    user = int(input(f"{a} * {b} = ?"))
    if user == c:
        print(f'Правильно! {c}')
        with open("results.txt", "a") as file:
           file.write(f"\n{a} * {b} = {user} . Правильно ({c})")
        tries -= 1
    elif user != c:
        print(f'Не правильно! {c}')
        with open("results.txt", "a") as file:
            file.write(f"\n{a} * {b} = {user} . Не правильно ({c})")
        tries -= 1
    end = datetime.datetime.now() - start
    if tries == 0:
        with open("results.txt", "a") as file:
            file.write(f"\nБыло {poputka} попыток, потраченное время: {end}. Имя: {name}")
