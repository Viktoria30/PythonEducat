# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     n= 5
#     1 2 3 4 5
#     x= 3
#     -> 1

n = int(input('Введите кол-во элементов в массиве: '))
list_A = [i + 1 for i in range(n)]
print(list_A)
x = 3
count = 0
for i in range(n):
    if list_A[i] == x:
        count =+1
print(f'Число {x} встечается {count} раз')

# второй вариант решения

list_nums = [int(input()) for _ in range(int(input()))]
print(list_nums.count(int(input())))

# третий вариант решения

from random import choices

num = int(input())
list_nums = choices(range(num * 2), k=num)
print(list_nums)

result = list_nums.count(int(input()))
print(result)
