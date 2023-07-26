# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
my_dict = {'Андрей': ('кружка', 'ложка', 'спальник', 'половник', 'сухари', 'рис'),
           'Борис': ('кружка', 'ложка', 'спальник', 'топор', 'сухари', 'гречка'),
           'Дима': ('кружка', 'ложка', 'спальник', 'палатка', 'сахар', 'гречка', 'рис')}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())

intersection_of_all = set(val_list[0])
for i in val_list:
    if i != 0:
        current_set = set(i)
        intersection_of_all = intersection_of_all.intersection(current_set)
print('Эти вещи взяли все три друга', intersection_of_all)

differ = {}
for i in val_list:
    temp = set(i)
    for j in val_list:
        if i != j:
            current_set = set(j)
            temp = temp.difference(current_set)
    position = val_list.index(i)
    key = key_list[position]
    differ[key] = temp
print('Эти вещи уникальны, есть только у одного друга', differ)

result3 = []
for i in val_list:
    temp = set(i)
    for j in val_list:
        if j != i:
            intersection_others = set[j]
            for k in val_list:
                if k != i:
                    current_set = set(k)
                    intersection_others = intersection_others.intersection(current_set)
    differ = intersection_others.difference(temp)
    position = val_list.index(i)
    key = key_list[position]
    print(f'Эти вещи есть у всех друзей {intersection_others}, у {key} нет {differ}' )