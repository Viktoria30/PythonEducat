# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Введите первый элемент: '))
d = int(input('Введите число прогрессии: '))
n = int(input('Введите кол-во элементов: '))

for i in range(n):
    print(a + i * d)
