# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Input year: '));

if year % 4 == 0:
	print(f'Year {year} is leap year.');
else:
	print(f'Year {year} is not leap year.');
