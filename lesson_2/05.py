# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

min_s = 32
max_s = 127
pos = 0
string = ''

for i in range(min_s, max_s + 1):
	string = string + ' | ' + "{0:0>3}".format(i) + ' | ' + chr(i)
	pos = pos + 1
	if pos == 10:
		print(string)
		string = ''
		pos = 0

print(string)