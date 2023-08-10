# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён
from random import randint,choice
from os import getcwd,listdir,mkdir,chdir


def give_name(min_len: int = 6,
         max_len: int = 30):
    name_ = ''
    for _ in range(randint(4,7)):
        name_ += chr(randint(98,122))
    return name_.capitalize()

def create_file(
         ext: str,
         directory: str = None,
         min_len: int = 6,
         max_len: int = 30,
         min_size:int = 256,
         max_size:int = 4096,
         count_files: int = 10

):
    if not directory:
        directory = getcwd() + '/'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '/' + directory + '/'
    print(directory)
    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w', encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0,255) for x in range(min_size,max_size)])
            output.write(str(list_of_bytes))

def create_random_ext_files():
    EXTENSIONS = ('.txt', '.doc', '.pdf')
    create_file(ext=choice(EXTENSIONS), directory='test_dir')


if __name__ == '__main__':
    create_random_ext_files()