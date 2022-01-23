"""
Дз Пункт 1
"""
class Phone:
    def __init__(self,camera ,color, flash):
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise ValueError('Camera should be float!!!')
        if isinstance(color,str):
            self.color = color
        else:
            raise ValueError("Color is string!!!")
        if isinstance(flash, bool):
            self.flash = flash
        else:
            raise ValueError('Flash is boolean!!!')

    def __str__(self):
        return f'Camera - {self.camera}\n'\
                f'Color - {self.color}\n'\
                f'Flash - {self.flash}\n'\

class Laptop(Phone):
    def __init__(self, camera, color, flash, mobility, memory):
        super().__init__(camera, color, flash)
        if isinstance(mobility,bool):
            self.mobility = mobility
        else:
            raise ValueError("Mobility is boolean!!!")
        if isinstance(memory, float):
            self.memory = memory
        else:
            raise ValueError("Memory is float!!!")

    def __str__(self):
        return super(Laptop, self).__str__() + f"Mobility - {self.mobility}\n"\
                                                f'Memory - {self.memory}\n'\

class Computer(Laptop):
    def __init__(self, camera, color, flash, mobility, memory, wires_Connect, keyboard ):
        super().__init__(camera, color, flash, mobility, memory)
        if isinstance(wires_Connect,bool):
            self.wires = wires_Connect
        else:
            raise ValueError("Wires Connect is booalean!!!")
        if isinstance(keyboard,bool):
            self.keyboard = keyboard
        else:
            raise ValueError("Keyboard is boolean!!!")

    def __str__(self):
        return super(Computer, self).__str__() + f'Wires Connect - {self.wires}\n'\
                                                f'Keyboard - {self.keyboard} \n' \

Iphone = Phone(4.2, "black", True)
print(Iphone)

Asus = Laptop(3.6 , "Gray" , True, True , 100.1)
print(Asus)

computer = Computer(0.0 , "Pink" , False, False, 200.1, True , True)
print(computer)

"""
Дз Пункт 2
"""

class Person:
    def __init__(self,name,virus):
        self.name = name
        self.__virus = virus

    def _virus1(self):
            pass

pers = Person(name="Leon", virus="Corona")
print(pers._virus1)


"""
ДЗ Пункт 3
"""

class Sportsman:
    def __init__(self,name, height, work):
        self.name = name
        self.height = height
        self.work = work

    def __str__(self):
        return          f"Name - {self.name}\n"\
                        f'Height - {self.height}\n'\
                        f'Work - {self.work}\n'\

class Boxer(Sportsman):

    def earning_money(self):
        return f"earning money with {self.work}\n"

class Swimmer(Sportsman):

    def earning_money(self):
        return f'earning money with {self.work}\n'

class Runner(Sportsman):

    def earning_money(self):
        return f'earning money with {self.work}\n'

    def earning_money2(self):
        return f'earning money by {self.work}'

class Dancer(Sportsman):

    def earning_momeny2
Box = Boxer("Mike",180, "boxing")
Run = Runner("John", 160 , "Running")
Swim = Swimmer("Kate", 170,"Swimming")
# print(Run.work)
# print(Swim.work)
# print(Box.work)
# print(Run)
# print(Swim)
# print(Box)

"""
ДЗ Пункт 4
"""

class Sportsman1:
    def __init__(self,name, height, work):
        self.name = name
        self.height = height
        self.work = work

    def __str__(self):
        return          f"Name - {self.name}\n"\
                        f'Height - {self.height}\n'\
                        f'Work - {self.work}\n'\

class Boxer1(Sportsman1):
    def __init__(self, name, height, work, boxing_burl, gloves):
        super().__init__(name, height, work)
        self.burl = boxing_burl
        self.gloves = gloves
    def __str__(self):
        return super(Boxer1, self).__str__() + f'Boxing Purl - {self.burl}\n'\
                                                f'Gloves - {self.gloves}\n'\

    def earning_money1(self):
        return f"earning money with {self.work}\n"


class Runner1(Boxer1):
    def __init__(self, name, height, work, boxing_burl, gloves, boots, mike):
        super().__init__(name, height, work, boxing_burl, gloves)
        self.boots = boots
        self.mike = mike
    def __str__(self):
        return super(Runner1, self).__str__() + f"Boots - {self.boots}\n"\
                                                f'Mike - {self.mike}\n'\

    def earning_money1(self):
        return f'earning money with {self.work}\n'

    def earning_money1(self):
        return f'earning money with {self.work}'
sportsm2 = Sportsman1("Georg", 178 , "Swimming")
boxer2 = Boxer1("Kone", 182, "Boxing", True, True)
runner2 = Runner1("Don" , 162 , "Running" , False , False, 'Nike' , True)
# print(sportsm2)
# print(boxer2)
# print(runner2)
# print(sportsm2.work)
# print(boxer2.work)
# print(runner2.work)




class CustomUser:
    ''