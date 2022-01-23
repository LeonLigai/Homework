Bishkek = input("Введите температуру в Чуйской области: ")
Osh = input("Введите температуру в Ошской области: ")
JalalAbad = input("Введите температуру в Джалал-Абадской области: ")
IsykKol = input("Введите температуру в Исык-Кульской области: ")
Naryn = input('Введите температуру в Нарынской области: ')
Talas = input("Введите температуру в Таласской области: ")
Batken = input("Введите температуру в Баткенской области: ")

Bishkek = float(Bishkek)
Osh = float(Osh)
JalalAbad = float(JalalAbad)
IsykKol = float(IsykKol)
Naryn = float(Naryn)
Talas = float(Talas)
Batken = float(Batken)

average = (Bishkek + Osh + JalalAbad + IsykKol + Naryn + Talas + Batken) / 7
average = round(average, 1)

print(f"Средний показатель температуры воздуха по КР на сегодня: {average}°C" )

