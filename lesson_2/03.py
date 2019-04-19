# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Input number: '))
newnumber = 0

while number > 0:
	cifra = number % 10
	number = number // 10
	newnumber = newnumber * 10
	newnumber = newnumber + cifra

print('New number: ', newnumber)