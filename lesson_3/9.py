# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

a = [[random.randint(1, 9) for i in range(0, 10)] for y in range(0, 10)]

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in a]))

min_a = []
for x in range(0, 10):
	min_a.append(10)
	for y in range(0, 10):
		if a[x][y] < min_a[x]:
			min_a[x] = a[x][y]

print(min_a)

max = 0
for x in range(0, 10):
	if max < min_a[x]:
		max = min_a[x]

print(max)