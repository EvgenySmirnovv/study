while True:# Усложнили задания. "Проверка правильности ввода данных"
    try:
        array = list(map(int, input("Введите целые числа, через пробел: ").split()))
        print("=====================")
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")
        print("=====================")

while True:# Проверка правильности ввода данных
    try:
        element = int(input("Введите число из списка для поиска"))
        print("=====================")
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")
        print("=====================")
array = sorted(array) # Прочитал и взял встроеную сортировку Timsort
def binary_search(array, element, left, right): # Взял двоичный поиск из матерала модуля.
    if left > right:  # если левая граница превысила правую
        return print("Числа нет в списке")
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

if element < array[0] or element > array[-1]: # Поиск числа в нужном диапозоне
    print('Числа нет в диапазоне')
else:
    print("Индекс числа:", binary_search(array, element, 0, len(array) - 1))
print("=====================")
print("Сортированный список", array) # Сортированные числа.