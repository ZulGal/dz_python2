# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from os import chdir, listdir, rename


def rename_file(
        wanted_name: str = 'video',
        count_nums: int = 4,
        extension_old: str = 'pdf',
        extension_new: str = 'csv',
        range_of_choice: list = [3, 6]):
    chdir('test_dir')
    count = 10 ** count_nums
    for file in listdir():
        if file.split('.')[1] == extension_old:
            count += 1
            new_name = file.split('.')[0][range_of_choice[0]:range_of_choice[1]] \
                       + wanted_name + str(count)[1:] + '.' + extension_new
            print(file, new_name)
            rename(file, new_name)


if __name__ == '__main__':
    rename_file()
