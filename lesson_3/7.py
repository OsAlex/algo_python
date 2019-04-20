# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

a = [random.randint(1, 10) for i in range(1, 10)]
min_num_1 = 10
min_num_2 = 10
min_pos_1 = 0
min_pos_2 = 0
i = 0
y = 0

for x in a:

    if x < min_num_1:
        min_num_1 = x
        min_pos_1 = i

        if min_num_1 < min_num_2:
            y = min_num_2
            min_num_2 = min_num_1
            min_num_1 = y

            y = min_pos_2
            min_pos_2 = min_pos_1
            min_pos_1 = y

    i = i + 1

print(a)
print('Min 1 : ', min_num_1, ' on ', min_pos_1, ' position')
print('Min 2 : ', min_num_2, ' on ', min_pos_2, ' position')
