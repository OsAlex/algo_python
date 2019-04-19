# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Input number: '))
chet = nechet = 0

while number > 0:
	cifra = number % 10
	number = number // 10
	if cifra % 2 == 0:
		chet = chet + 1
	else:
		nechet = nechet + 1

print('Chet: ', chet, ' Nechet: ', nechet)