# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('input n: '))
i = 0
y = 1
summa = 0

while i < n:
	summa = summa + y
	y = y * -.5
	i = i + 1


print('Summa: ', summa, 'iterations: ', i)