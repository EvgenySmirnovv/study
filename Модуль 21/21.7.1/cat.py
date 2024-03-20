from pets import Cat

pet1 = Cat("Барон", "мальчик", 2)

print("Имя первого кота -", pet1.getName())
print("Пол первого кота -", pet1.getGender())
print("Возраст первого кота", pet1.getAge())

print()

pet2 = Cat("Сэм", "мальчик", 2)

print("Имя второго кота -", pet2.getName())
print("Пол второго кота -", pet2.getGender())
print("Возраст второго кота", pet2.getAge())
