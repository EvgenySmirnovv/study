class Rec:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea_Rec(self):
        return self.a * self.b
#Сделали площадь прямоугольника
class Squ:
    def __init__(self, a):
        self.a = a

    def getArea_Squ(self):
        return self.a ** 2
#Сделали площадь квадарат(Добавили по заданию)
class Cir:
    def __init__(self, a):
        self.a = a
    def getArea_Cir(self):
        return 3.14 * (self.a ** 2)
#Сделали площадь круга(Добавили по заданию еще раз)
class Tri:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) / 2  #полупериметр
    def getArea_Tri(self):
        return  (self.p *((self.p-self.a) * (self.p-self.b) * (self.p-self.c))) ** 0.5
#Сделали площадь треугольнка по формуле герона(Добавил дополнительно от себя)
