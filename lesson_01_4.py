# 4. Написать программу, которая генерирует в указанных пользователем границах:
#  случайное целое число;
#  случайное вещественное число;
#  случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти 
# символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

n = input('Input from: ');
m = input('Input to: ');

if n.isdigit() and m.isdigit():
	print('Random from ', n, ' to ', m, ' = ', random.randint(int(n),int(m)));

else:
	try:
	    x = float(n)
	    x = float(m)
	except ValueError as err:
	    x = False  

	if x:
		print('Random from ', n, ' to ', m, ' = ', random.uniform(float(n),float(m)));
	else:
		print('Random from ', n, ' to ', m, ' = ', chr(random.randint(ord(n), ord(m))));