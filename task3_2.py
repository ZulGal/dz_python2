# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)
text = 'Дополнительное: \
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:\
* Какие вещи взяли все три друга \
* Какие вещи уникальны, есть только у одного друга \
* Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует \
* Для решения используйте операции с множествами. \
Код должен расширяться на любое большее количество друзей.'
# import string library function
import string

LIMIT_RATE = 10
text = text.lower()

# Use the combo of translate() and maketrans() method
text = text.translate(str.maketrans('', '', string.punctuation))
my_dict = {}
for i in text.split():
    my_dict[i] = text.count(i)
print(my_dict)
rate_dict = {'0': 0}
for i in my_dict:
    if my_dict[i] > min(rate_dict.values()):
        if len(rate_dict) < LIMIT_RATE:
            rate_dict[i] = my_dict[i]
        else:
            key_list = list(rate_dict.keys())
            val_list = list(rate_dict.values())
            position = val_list.index(min(rate_dict.values()))
            key = key_list[position]
            spam = rate_dict.pop(key)
            rate_dict[i] = my_dict[i]
print(rate_dict)
