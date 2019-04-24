# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for x in range(2,100):
	aliquot = 0
	
	for y in range(2,100):
		if x % y == 0:
			aliquot = aliquot + 1

	print(f'{x} aliquot {aliquot} numbers from 2 to 99')
