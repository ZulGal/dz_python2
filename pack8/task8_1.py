#
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
#
#
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
#     "name": names.txt
#     "parent": users,
#     "type": "file"
#     "size": 4096
# }
#
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def content_of_dir(namedir:str) -> None:
    data: list = [{'name': namedir, 'parent': None,'type': 'dir','size': get_size(namedir)}]
    os.chdir(f'{os.path.join(os.getcwd(),namedir)}')

    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        data.extend({'name': i, 'parent': dir_path.split('/')[-1],'type': 'file', \
                     'size': os.path.getsize(f'{os.path.join(dir_path,i)}')} for i in file_name)
        data.extend({'name': i, 'parent': dir_path.split('/')[-1],'type': 'dir','size': get_size(i)} for i in dir_name)
    print(f'{data=}')

    os.chdir('..')
    print(os.getcwd())
    with (
        open ('dz8_out.json', 'w', encoding='utf-8') as out_json,
        open ('dz8_out.csv', 'w', newline='', encoding='utf-8') as out_csv,
        open('dz8_out.pickle', 'wb') as out_pickle
    ):
        json.dump(data, out_json, indent=4)
        csv_write = csv.DictWriter(out_csv, fieldnames=["name", "parent","type","size"],
                                   dialect='excel-tab', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(data)
        pickle.dump(data, out_pickle)




if __name__ == '__main__':
    content_of_dir('dir')