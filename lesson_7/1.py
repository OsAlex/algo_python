# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random
import timeit


def sort_d(a):
    length_a = len(a)

    for index in range(length_a - 1):
        for index_1 in range(length_a - index - 1):
            # print(index_1, a)
            if a[index_1] < a[index_1 + 1]:
                a[index_1 + 1], a[index_1] = a[index_1], a[index_1 + 1]

    return a


def sort_d_1(a):

    len_a = len(a)
    if len_a < 2:
        return a

    small = []
    big = []
    for index_1 in range(len_a - 1, 0, -1):
        if a[index_1] > a[0]:
            big.append(a[index_1])
        else:
            small.append(a[index_1])

    # print(big, small)
    a = sort_d_1(big) + [a[0]] + sort_d_1(small)

    return a


a = [random.randint(0, 10) for i in range(1, 10)]

print(a)
a = sort_d(a)
print(a)

a = [random.randint(0, 10) for i in range(1, 10)]

print(a)
a = sort_d_1(a)
print(a)

a = [random.randint(0, 10) for i in range(1, 10)]
print(timeit.timeit("sort_d(a)", setup="from __main__ import sort_d, a", number=10000))

a = [random.randint(0, 10) for i in range(1, 10)]
print(timeit.timeit("sort_d_1(a)", setup="from __main__ import sort_d_1, a", number=10000))

# sort_d_1 - попробовал сделать через рекурсию, сортирует - но работает дольше чем пузырьком