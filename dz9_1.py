# Напишите следующие функции:
#
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from random import randint
import decimal
from cmath import sqrt


def count(num: int = 1):
    def deco(func: callable):
        def wrapper(*args, **kwargs):
            data = []
            for i in range(num):
                result = [func(*args, **kwargs) for i in range(3)]
                data.append(result)
            print(f'{data= }')
            with open('dz9_file.csv', 'w', newline='', encoding='utf-8') as out_csv:
                csv_write = csv.writer(out_csv, dialect='excel')
                csv_write.writerows(data)
            return result

        return wrapper
    return deco


@count(5)
def get_random_coeff(a: int, b: int):
    return randint(a, b)


def solution(func: callable):
    def wrapper(a_, b_, c_):
        data: dict = {}
        with open('dz9_file.csv', 'r', newline='') as inp_csv:
            csv_file = csv.reader(inp_csv, quoting=csv.QUOTE_NONNUMERIC)
            for line in csv_file:
                a_, b_, c_ = line
                arg = str(line)
                res = func(a_, b_, c_)
                data.update({arg: res})
        with open('dz9_file.json', 'w', encoding='utf-8') as out_json:
            json.dump(data, out_json, ensure_ascii=False, indent=4)
        return func(a_, b_, c_)

    return wrapper


@solution
def roots_quadratic(a: float, b: float, c: float):
    d = (b ** 2 - 4 * a * c)
    if d != 0:
        x1 = (-b + sqrt(d)) / 2 / a
        x2 = (-b - sqrt(d)) / 2 / a
        result = "2 корня: x1 = " + str(x1) + "и x2 = " + str(x2)
    else:
        x = decimal.Decimal(-b / 2 / a)
        result = "1 корень: " + str(x)
    return result


if __name__ == '__main__':
    get_random_coeff(1, 10)
    roots_quadratic(1, 1, 1)
