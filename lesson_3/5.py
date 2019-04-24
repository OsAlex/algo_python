# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-10, i) for i in range(1, 10)]
b = {}
i = 0
max_num = {
    'value': -10,
    'index': 0,
}

for x in a:
    if x < 0 and x > max_num['value']:
        max_num['value'] = x
        max_num['index'] = i
    i = i + 1

print('In array: ', a)
# print(b)
print('Max negative number ', max_num['value'],
      ' on ', max_num['index'], ' position')
