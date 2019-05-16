# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import string
import random
import hashlib

str_rand = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
print(str_rand)

substrings = {}

for j in range(0, len(str_rand)+1):
    for i in range(j+1, len(str_rand)+1):
        substring = str(str_rand[j:i]).encode('utf-8')
        substrings[hashlib.md5(substring).hexdigest()] = str_rand[j:i]

print('String: ', str_rand, ' has ', len(substrings), ' substrings:')
print(list(substrings.values()))
