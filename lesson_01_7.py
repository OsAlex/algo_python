# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. 
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Input first side: '));
b = int(input('Input second side: '));
c = int(input('Input third side: '));

sides = [a, b, c];
# Get max side 
maxSide = max(sides);
# Get other sides
sides.remove(maxSide);

if maxSide >= sum(sides):
	print('the possibility of the existence of a triangle is negative. Because sum of two sides < max side.');
else:
	print('the possibility of the existence of a triangle is positive.  Because sum of two sides > max side.')

	if sides[0] == sides[1]:
		if sides[0] == maxSide:
			print('This triangle is equilateral');
		else:
			print('This triangle is isosceles');
	else:
		print('This triangle is versatile');