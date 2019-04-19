# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

while True:
	x = random.randint(0,100)

	for i in range(1,11):
		n = int(input('input n: '))
		if x < n :
			print('It`s big')
		elif x > n:
			print('It`s small')
		else:
			print('You win')
			exit()

	print('You loose. It`s ', x)
	n = input('Next round? input y/n : ')
	if n != 'y':
		exit()
