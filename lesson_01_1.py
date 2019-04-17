
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

chislo = '';

while len(chislo) != 3:
	chislo = input('Enter a three-digit number: ');


summa = int(chislo[0]) + int(chislo[1]) + int(chislo[2])
print('The sum of the digits of three digits: ', summa);

comp = int(chislo[0]) * int(chislo[1]) * int(chislo[2])
print('The composition of the digits of a three-digit number: ', comp);



