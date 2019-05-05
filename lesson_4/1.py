# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit

def get_sum_between_min_max_1(a):
    min_num = 10
    max_num = 0
    min_pos = 0
    max_pos = 0
    i = 0

    for x in a:
        if x < min_num:
            min_num = x
            min_pos = i
        if x > max_num:
            max_num = x
            max_pos = i
        i = i + 1

    # print('Array: ', a)
    # print('Max number ', max_num, ' on ', max_pos, ' position')
    # print('Min number ', min_num, ' on ', min_pos, ' position')

    if min_pos < max_pos:
        range_y = range(min_pos + 1, max_pos)
    else:
        range_y = range(max_pos + 1, min_pos)

    summa = 0

    for y in range_y:
        # print('on ', y, ' position ', a[y])
        summa = summa + a[y]

    # print('Sum elements from min to max elements: ', summa)
    return summa


def get_sum_between_min_max_2(a):
    min_pos = a.index(min(a))
    max_pos = a.index(max(a))

    if min_pos < max_pos:
        return sum(a[min_pos + 1:max_pos])
    else:
        return sum(a[max_pos + 1:min_pos])


a = [random.randint(1, 10) for i in range(1, 10)]
print(timeit.timeit("get_sum_between_min_max_1(a)", setup="from __main__ import get_sum_between_min_max_1, a", number=10000))
print(timeit.timeit("get_sum_between_min_max_2(a)", setup="from __main__ import get_sum_between_min_max_2, a", number=10000))


a = [random.randint(1, 100) for i in range(1, 100)]
print(timeit.timeit("get_sum_between_min_max_1(a)", setup="from __main__ import get_sum_between_min_max_1, a", number=10000))
print(timeit.timeit("get_sum_between_min_max_2(a)", setup="from __main__ import get_sum_between_min_max_2, a", number=10000))


a = [random.randint(1, 1000) for i in range(1, 1000)]
print(timeit.timeit("get_sum_between_min_max_1(a)", setup="from __main__ import get_sum_between_min_max_1, a", number=10000))
print(timeit.timeit("get_sum_between_min_max_2(a)", setup="from __main__ import get_sum_between_min_max_2, a", number=10000))


# Второй алгоритм использует встроенные функции и использует меньше переменных, 
# поэтому работает быстрее и время работы медленнее возрастает при увеличении данных

# при массиве из 10 элементов
# 0.018037721
# 0.014291674999999997


# при массиве из 100 элементов
# 0.10160356799999999
# 0.059798900000000016

# при массиве из 1000 элементов
# 1.204463749
# 0.658393035

