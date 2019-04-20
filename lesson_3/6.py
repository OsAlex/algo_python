# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(1, 10) for i in range(1, 10)]
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

print('Array: ', a)
print('Max number ', max_num, ' on ', max_pos, ' position')
print('Min number ', min_num, ' on ', min_pos, ' position')

if min_pos < max_pos:
    range_y = range(min_pos+1, max_pos)
else:
    range_y = range(max_pos+1, min_pos)

summa = 0

for y in range_y:
    print(y, ':', a[y])
    summa = summa + a[y]

print('Sum elements from min to max elements: ', summa)