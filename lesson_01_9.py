# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Input first int: '));
b = int(input('Input second int: '));
c = int(input('Input third int: '));

numbers = [a, b, c];
minNumber = min(numbers);
maxNumber = max(numbers);

numbers.remove(minNumber);
numbers.remove(maxNumber);

print(f'Average number is {numbers}');