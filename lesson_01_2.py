# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. 
# Объяснить полученный результат.

i = 5 & 6
print('5 = ', bin(5),', 6 = ', bin(6), ', 5 & 6 = ', bin(i), ' = ', i)

i = 5 | 6
print('5 = ', bin(5),', 6 = ', bin(6), ', 5 | 6 = ', bin(i), ' = ', i)

i = 5 << 2
print('Print 5 << 2: ', bin(5), ' << 2 = ', bin(i), ' = ', i)

i = 5 >> 2
print('Print 5 >> 2: ', bin(5), ' >> 2 = ', bin(i), ' = ', i)