# 4. Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(1, i) for i in range(1, 10)]
b = {}
i = 0
max_num = {
    'value': 0,
    'index': 0,
}

for x in a:
    if x in b:
        b[x] = b[x] + 1
    else:
        b[x] = 1

    if b[x] > max_num['value']:
        max_num['value'] = b[x]
        max_num['index'] = x

print('In array: ', a)
# print(b)
print('Number ', max_num['index'], ' repeat ', max_num['value'], ' times')
