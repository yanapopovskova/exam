import math
import re

with open('input.txt') as f:
    s = f.read().split(' ')

# Обработка: Распознать через регулярные выражения натуральные четные двоичные числа,
# в которых вторая и предпоследняя цифра равны 1, из которых определить минимальное число и их количество.

result = []
min_num = math.inf
min_num_str = ''
for num_str in s:
    print(num_str)
    if re.fullmatch(r'([01]1[01]*10)|([01]10)', num_str):
        result.append(num_str)
        num = int(num_str, 2)
        if min_num > num:
            min_num = num
            min_num_str= num_str

print('Количество искомых чисел:', len(result))
print('Минимальное такое число:', min_num_str)
