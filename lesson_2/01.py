# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
	znak = input('Input symbol of operation: ')

	while znak not in ['0', '+', '-', '*', '/'] :
		print("Error in input, choise '0', '+', '-', '*', '/'.\n")
		znak = input('Input symbol of operation: ')

	if znak == '0' :
		print('The End')
		exit()

	chislo1 = int(input('Input first argument: '))
	chislo2 = int(input('Input second argument: '))

	if znak == '+' :
		result = chislo1 + chislo2 
	elif znak == '-' :
		result = chislo1 - chislo2
	elif znak == '*' :
		result = chislo1 * chislo2
	elif znak == '/' :
		if chislo2 == 0:
			print('Division by zero is prohibited')
			result = ''
		else:
			result = chislo1 / chislo2

	print('Result: ', result, "\n")
