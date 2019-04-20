# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(1, i) for i in range(1,10)]
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

print(a)
a[max_pos] = min_num
a[min_pos] = max_num
print(a)