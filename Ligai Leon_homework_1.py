class Animal:
    def __init__(self, fangs, wool , predator, ):
        if isinstance(fangs,bool):
            self.fangs = fangs
        else:
            raise ValueError("Fangs should be boolean!!")
        if isinstance(wool,str):
            self.wool = wool
        else:
            raise ValueError("Wool should be string!!!")
        if isinstance(predator, bool):
            self.predator = predator
        else:
            raise ValueError("Predator should be boolean!!!")

    def __str__(self):
        return f'Wool = {self.wool}\n'\
                f'Fangs = {self.fangs}\n'\
                f"Predator = {self.predator}\n"\

Wolf = Animal(True, "Yes" , True)
print(Wolf)

class Mlekopit(Animal):
    def __init__(self, fangs, wool, predator, fin, hair , ears):
        super().__init__(fangs, wool, predator)
        if isinstance(fin, bool):
            self.fin = fin
        else:
            raise ValueError("Fin should be boolean!!!")
        if isinstance(hair, bool):
            self.hair = hair
        else:
            raise ValueError("Hair should be boolean!!!")
        if isinstance(ears, bool):
            self.ear = ears
        else:
            raise ValueError("Ears should be boolean!!!")

    def __str__(self):
        return super(Mlekopit,self).__str__() +  f'Fin = {self.fin}\n'\
                                                f'Hair = {self.hair}\n'\
                                                f'Ears = {self.ear}\n'\

man = Mlekopit(False, "No", False, False, True, True )
print(man)


class Presmik(Animal):
    def __init__(self, fangs, wool, predator, fin, tail , scale):
        super().__init__(fangs, wool, predator)
        if isinstance(fin, bool):
            self.fin = fin
        else:
            raise ValueError("Fin should be boolean!!!")
        if isinstance(scale, bool):
            self.scale = scale
        else:
            raise ValueError("Scale should be boolean!!!")
        if isinstance(tail, bool):
            self.tail = tail
        else:
            raise ValueError("Tail should be boolean!!!")

    def __str__(self):
        return super(Presmik,self).__str__() +  f'Fin = {self.fin}\n'\
                                                f'Tail = {self.tail}\n'\
                                                f'Scale = {self.scale}\n'\


Turtle = Presmik(False,'No',False,False, True, True )
print(Turtle)
    def __str__(self):
        одл