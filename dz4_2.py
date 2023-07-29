# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def only_kwargs(**kwargs) -> dict:
    list_unhashable = ['bytarray', 'dict', 'list', 'set']
    my_dict = {}
    for key, value in kwargs.items():
        if type(value in list_unhashable):
            my_dict[str(value)] = key
        else:
            my_dict[value] = key
    return my_dict


print(only_kwargs(name='Андрей', salary=100_000, age=30))
print(only_kwargs(name=[1, 2, 3]))
