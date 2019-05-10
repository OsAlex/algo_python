# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. 
# Результаты анализа вставьте в виде комментариев к коду. 
# Также укажите в комментариях версию Python и разрядность вашей ОС.


# Python 3.7.2
# OS - Windows 64

import random

@profile
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

    if min_pos < max_pos:
        range_y = range(min_pos + 1, max_pos)
    else:
        range_y = range(max_pos + 1, min_pos)

    summa = 0

    for y in range_y:
        summa = summa + a[y]

    return summa


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    get_sum_between_min_max_1(a)



# python -m memory_profiler 2.py
# Filename: 2.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     13   14.426 MiB   14.426 MiB   @profile
#     14                             def get_sum_between_min_max_1(a):
#     15   14.426 MiB    0.000 MiB       min_num = 10
#     16   14.426 MiB    0.000 MiB       max_num = 0
#     17   14.426 MiB    0.000 MiB       min_pos = 0
#     18   14.426 MiB    0.000 MiB       max_pos = 0
#     19   14.426 MiB    0.000 MiB       i = 0
#     20
#     21   14.426 MiB    0.000 MiB       for x in a:
#     22   14.426 MiB    0.000 MiB           if x < min_num:
#     23   14.426 MiB    0.000 MiB               min_num = x
#     24   14.426 MiB    0.000 MiB               min_pos = i
#     25   14.426 MiB    0.000 MiB           if x > max_num:
#     26   14.426 MiB    0.000 MiB               max_num = x
#     27   14.426 MiB    0.000 MiB               max_pos = i
#     28   14.426 MiB    0.000 MiB           i = i + 1
#     29
#     30   14.426 MiB    0.000 MiB       if min_pos < max_pos:
#     31   14.426 MiB    0.000 MiB           range_y = range(min_pos + 1, max_pos)
#     32                                 else:
#     33                                     range_y = range(max_pos + 1, min_pos)
#     34
#     35   14.426 MiB    0.000 MiB       summa = 0
#     36
#     37   14.426 MiB    0.000 MiB       for y in range_y:
#     38                                     summa = summa + a[y]
#     39
#     40   14.426 MiB    0.000 MiB       return summa
