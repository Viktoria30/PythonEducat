# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     n = 5
#     1 2 3 4 5
#     x = 6
#     -> 5

n = int(input('Введите кол-во элементов в массиве: '))
list_A = [i + 1 for i in range(n)]
print(list_A)
x = 3 
for i in range(len(list_A)):
    b = list_A[i] - x
print(f'Не получается решить')

# решение 2 

from random import randint

list_nums = [randint(1, 21) for _ in range(int(input()))]

print(list_nums)
num = int(input())
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print(right_num)

# решение 3


from random import randint

n = int(input())
list_nums = [randint(1, 50) for _ in range(int(input()))]

print(list_nums)

b = int(input())
m = min(list_nums, key=lambda x: abs(x - b))

print(m)
