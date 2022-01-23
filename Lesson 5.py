import re


my_text = "Vasya, 1997, vasya@gmail.com,4000$, male* " \
            "Adilet, 1997 , adilet@intel.ru, 50002323$, male* " \
            "Aidana, 2000, aidana@yandex.ru , 89764543$ , female% "\
            'Aman, 1999, aman@mail.ru,789$ , male* ' \
            'Regina, 1999, regina@yahoo.ru, 69$, female% ' \
            'Lol, 5434 , lol@gmail.com, 9087$ , female% '

"""
\d --Он ишет подряд стоящие ЧИСЛА [0-9]
\D -- Он ищет любые, но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\W -- Любой не алфавитны символ
\s -- Ищет пробелы 
\S -- Специальные символы
"""

what_search = r'[5-9]'
results = re.findall(what_search, my_text)
print(results)