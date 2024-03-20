from rectangle import Rec, Squ, Cir, Tri

Rec1 = Rec(5,6)

print("Площадь первого прямоугольника", Rec1.getArea_Rec())
print("__________")

Rec2 = Rec(10,20)
print("Площадь второго прямоугольника", Rec2.getArea_Rec())
print("__________")

Sqa1 = Squ(6)
print("Площадь первого квадрата", Sqa1.getArea_Squ())
print("__________")

Squ2 = Squ(15)
print("Площадь второго квадрата", Squ2.getArea_Squ())
print("__________")

Cir1 = Cir(6)
print("Площадь первого круга", Cir1.getArea_Cir())
print("__________")

Cir2 = Cir(13)
print("Площадь второго круга", Cir2.getArea_Cir())
print("__________")

Tri1 = Tri(4,5,6)
print("Площадь перовго треугольника", Tri1.getArea_Tri())
print("__________")

Tri2 = Tri(6,5,8)
print("Площадь второго треугольника", Tri2.getArea_Tri())
print("__________")
