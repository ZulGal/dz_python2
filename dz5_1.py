# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from os import path


def get_path_name_ext(link_: str) -> tuple:
    full_name = path.basename(link_)
    name_ = path.splitext(full_name)[0]
    extension = path.splitext(full_name)[1]
    index_ = link_.index(name_)
    path_ = link_[:index_]
    return (path_, name_, extension)


link = r'/home/svetlana/geekbrains2/pytnon3.10/seminar/task3_2.py'
print(get_path_name_ext(link))
