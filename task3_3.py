# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools
from itertools import permutations

LIMIT_WEIGHT = 10
my_dict = {'спальник': 1, \
           'тушенка': 3, 'сгущенка': 2, \
           'гречка': 3,'сахар': 1,'рис':2,\
           'топор': 1, 'палатка': 4}
key_list = list(my_dict.keys())
val_list = list(my_dict.values())

for k in range(1, len(my_dict) + 1):
    seq = permutations(val_list, k)

    differ = LIMIT_WEIGHT
    nearest_sum = 0
    nearest_p = ()
    for p in list(seq):
        current_sum = 0
        for i in p:
            current_sum += i
        if current_sum <= LIMIT_WEIGHT:
            if LIMIT_WEIGHT - current_sum < differ:
                differ = LIMIT_WEIGHT - current_sum
                nearest_sum = current_sum
                nearest_p = p
        else:
            break
    result = ''
    for i in nearest_p:
        position = val_list.index(i)
        key = key_list[position]
        result += f'{key}: {my_dict[key]},'
    if nearest_sum != 0:
        print('Количество предметов=', k, ', Лимит= ', LIMIT_WEIGHT, '-', result, 'Общий вес = ', nearest_sum)
    else:
        print('Количество предметов=', k, ', Лимит= ', LIMIT_WEIGHT, '-', result, 'Общий вес превышает лимит')
    nearest_sum = LIMIT_WEIGHT
