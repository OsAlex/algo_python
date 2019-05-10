# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. 
# Результаты анализа вставьте в виде комментариев к коду. 
# Также укажите в комментариях версию Python и разрядность вашей ОС.


# Python 3.7.2
# OS - Windows 64

import random
import timeit
from pympler import asizeof
from pympler import tracker

tr = tracker.SummaryTracker()

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
    print('Sum size variables in memory: ', asizeof.asizeof(min_num) + asizeof.asizeof(max_num) + asizeof.asizeof(min_pos) + asizeof.asizeof(max_pos) + 
    	asizeof.asizeof(i) + asizeof.asizeof(x) + asizeof.asizeof(a) + asizeof.asizeof(range_y) + asizeof.asizeof(y))

    return summa


def get_sum_between_min_max_2(a):
    min_pos = a.index(min(a))
    max_pos = a.index(max(a))

    print('Sum size variables in memory 2: ', asizeof.asizeof(min_pos) + asizeof.asizeof(max_pos) + asizeof.asizeof(a))

    if min_pos < max_pos:
        return sum(a[min_pos + 1:max_pos])
    else:
        return sum(a[max_pos + 1:min_pos])


a = [random.randint(1, 10) for i in range(1, 10)]
print(timeit.timeit("get_sum_between_min_max_1(a)", setup="from __main__ import get_sum_between_min_max_1, a", number=1))
print(timeit.timeit("get_sum_between_min_max_2(a)", setup="from __main__ import get_sum_between_min_max_2, a", number=1))


tr.print_diff()



# memory_profiler дает разные результаты от запуска к запускуно в среднем:
# первый вариант: 14.426 MiB  
# второй вариант: 14.410 MiB

# asizeof:

# первый вариант:
# Sum size variables in memory:  336

# второй вариант:
# Sum size variables in memory 2:  232

#                                  types |   # objects |   total size
# ====================================== | =========== | ============
#                           <class 'list |        2330 |    118.40 KB
#                            <class 'str |        2328 |    106.54 KB
#                           <class 'type |         114 |     59.67 KB
#                          <class 'tuple |         212 |      7.88 KB
#                           <class 'dict |          29 |      5.38 KB
#                        <class 'weakref |         115 |      4.94 KB
#                            <class 'int |         295 |      4.28 KB
#              <class 'getset_descriptor |          17 |    680     B
#                          <class 'bytes |          12 |    325     B
#             <class 'wrapper_descriptor |           4 |    176     B
#                           <class 'code |           2 |    168     B
#                  function (store_info) |           1 |     72     B
#   function (get_sum_between_min_max_1) |           1 |     72     B
#   function (get_sum_between_min_max_2) |           1 |     72     B
#                           <class 'cell |           2 |     56     B
