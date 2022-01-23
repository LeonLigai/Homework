"""
1 задача
"""
class Mersedes:
    def __init__(self, model, power, weight, colour):
        if isinstance(model, str):
            self.model = model
        else:
            raise Exception('Model is string')
        if isinstance(power, int):
            self.power = power
        else:
            raise ValueError('Power is integer')
        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('Weight is integer')
        if isinstance(colour, str):
            self.colour = colour
        else:
            raise Exception('Colour is string')
    def __str__(self):
        return f'Model: {self.model}\n' \
               f'Power: {self.power}\n' \
               f'Weight: {self.weight} tons\n' \
               f'Colour: {self.colour}\n'

mers = Mersedes(model='c', power=156, weight=1, colour='black')
print(mers)

class SportMers(Mersedes):
    def __init__(self, model, power, weight, colour):
        super().__init__(model, power, weight, colour)
    def Colour_PLus(self, colour_plus):
        if colour_plus == self.colour:
            return 'All info!'

    def __str__(self):
        return super(SportMers, self).__str__()
sport = SportMers(model='c', power=156, weight=1, colour='black')
print(sport)
print(sport.Colour_PLus('red'))

class Coast(Mersedes):
    def __init__(self, model, power, weight, colour):
        super().__init__(model, power, weight, colour)
    def coast(self):
        return f'coast is 15000 $'
    def __str__(self):
        return super(Coast, self).__str__()

class Plus_Power(Coast, Mersedes):
    def __init__(self, model, power, weight, colour):
        super().__init__(model, power, weight, colour)
    def __str__(self):
        return super(Plus_Power, self).__str__()

plus_power = Plus_Power(model='c', power=156, weight=1, colour='black')
print(plus_power)
print(plus_power.coast())


"""
2 задача.
"""
class Kinder_garden:
    def __init__(self, number, name, age_of_students, number_of_students):
        self.number = number
        self.name = name
        self.age = age_of_students
        self.number_s = number_of_students

    def capacity(self):
        return f'В {self.name} могут учиться {self.number_s} человек '

    def results(self):
        return f'Когда заканчивают садик , дети умеют общаться с ровесниками '

    def __str__(self):
        return f'№ : {self.number}\n' \
               f'Name : {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Students: {self.number_s}\n'
kin_gard = Kinder_garden(number=29, name='Ромашка', age_of_students='2 - 5', number_of_students='100')
print(kin_gard)

class School(Kinder_garden):
    def __init__(self, number, name, age_of_students, number_of_students, document, language):
        super(School, self).__init__(number, name, age_of_students, number_of_students)
        self.doc = document
        self.lang = language

    def languages(self):
        return f'Заведение с углубленным изучением {self.lang} язык(а)'


    def results(self):
        return f'По окончанию школы выдается {self.doc}'

    def __str__(self):
        return super(School, self).__str__() + f'Doc: {self.doc}\nlang: {self.lang}'


school = School(number=17, name='Имени Пушкина', age_of_students='6 - 17', number_of_students='2400', document='Grade 11 attestat', language='Русского')
print(school.results())

class College(Kinder_garden):
    def __init__(self, number, name, age_of_students, number_of_students, document, faculty: list):
        super(College, self).__init__(number, name, age_of_students, number_of_students)
        self.doc = document
        self.fac = faculty

    def results(self):
        return f'По окончанию колледжа выдается {self.doc}'

    def fac(self):
        return f'у колледжа есть {self.fac} факультеты'

    def __str__(self):
        return super(College, self).__str__() + f'Doc: {self.doc}\nfaculty: {self.fac}'

college_1 = College(number=24, name='Имени Ломоносова', age_of_students='16 - 19', number_of_students='2700', document='Среднее профессиональное ', faculty=[
    'ГидроСтроительный',
    'Авиационный',
    'Инженерный'
])
print(college_1)

class University(Kinder_garden):
    def __init__(self,number, name, age_of_students, number_of_students, document, faculty, practice):
        super(University, self).__init__(number, name, age_of_students, number_of_students)
        self.doc = document
        self.fac = faculty
        self.prac = practice
    def results(self):
        return f'По окончанию университета выдается {self.doc}'

    def fac(self):
        return f'у университета есть {self.fac} факультет'

    def prac(self):
        return f'У университета есть практика по {self.prac}'

    def __str__(self):
        return super(University, self).__str__() + f'Doc: {self.doc}\nFac: {self.fac}\n Practice: {self.prac}'

univer = University(number=34, name='Имени Ломоносова', age_of_students='16 - 19', number_of_students='2700', document='Среднее профессиональное ', faculty=
'Авиационный',practice='Эксплуатация аппаратов')
print(univer)

"""
3 задача.
"""

class Cinema:
    def __init__(self, id, name, genre, coast, year, session, country):
        self.name = name
        self.genre = genre
        self.coast = coast
        self.year = year
        self.ses = session
        self.country = country
        self.id = id

    def information(self):
        return f'Film {self.name} начинается в {self.ses}, цена {self.coast}$'


    def __str__(self):
        return f'ID: {self.id}\n'\
               f'Name: {self.name}\n' \
               f'Genre: {self.genre}\n' \
               f'Coast: {self.coast}\n' \
               f'Year: {self.year}\n' \
               f'Session: {self.ses}\n' \
               f'Country: {self.country}\n'
spider = Cinema(id=1, name='SpiderMan', genre='fantasy', coast=2, year=2021, session='14:15', country='USA')
venom = Cinema(id=2, name='Venom', genre='fantasy', coast=3, year=2021, session='17:30', country='Canada')
one_plus_one = Cinema(id=3, name='1 + 1', genre='dram', coast=2.3, year=2011, session='18:30', country='Frans')

movies = (spider, venom, one_plus_one)

def choice(id):
    for i in movies:
        if i.id == id:
            return i.information()
    return "Такого фильма не существует!"

for i in movies:
    print(i)
while True:
    a = int(input('Выберите фильм по ID, введите 0 для выхода: '))
    print(choice(a))
    if a == 0:
        break


class StarBucks:
    def __len__(self, string_some):
        if len(string_some) >= 9:
            string_some = string_some[:5]
        elif len(string_some) < 5:
            string_some = string_some[-3:]
        return string_some

p1 = StarBucks()
p2 = StarBucks()
p3= StarBucks()
p4 = Mersedes("c2", 33, 2,"red")
print(p1.__len__('Leon'))
print(p2.__len__('Leo'))
print(p3.__len__("Ledss"))
print(p4)

gribe = mers("f")