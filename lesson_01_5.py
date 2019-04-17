# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

n = input('Input first letter: ');
m = input('Input last letter: ');

place_n = ord(n) - ord('a') + 1;
place_m = ord(m) - ord('a') + 1;

print(n, ' on ', place_n, ' place, ', m, ' on ', place_m, ' place. Between ', n, ',', m, ' - ', place_m - place_n, ' letters.');