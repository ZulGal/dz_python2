# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву
#   и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра.
#   Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5)
#   и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета
#   и по оценкам всех предметов вместе взятых.
import csv


class Range_fio:
    def validate(self, value):
        if not value[0].isupper():
            raise ValueError(f'Первая буква {value} должна быть заглавной')
        if not value.isalpha():
            raise ValueError(f'{value} должна состоять только из букв')


class Range_disc:
    def __init__(self, list_disc: list):
        self.list_disc = list_disc
        print('1', list_disc)

    def __repr__(self):
        return f'Range_disc(list_disc={self.list_disc}'

    def validate(self, value):
        if not value in self.list_disc:
            raise ValueError('Значение выходит за пределы заданных параметров'
                             f'от {self.list_disc}')


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not self.min_value < value < self.max_value:
            raise ValueError('Значение  выходит за пределы заданных параметров'
                             f' от {self.min_value}   до {self.max_value}')


class Student:
    surname = Range_fio()
    name = Range_fio()
    patronymic = Range_fio()

    discipline = []
    with open('dz12.csv', 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for line in csv_file:
            discipline.append(line[0])
    print('2', discipline)

    achievement = {}
    for key in achievement:
        key = Range_disc(discipline)

    for key in achievement:
        achievement[key][0] = Range(2, 5)
        achievement[key][1] = Range(0, 100)

    def __init__(self, surname: str, name: str, patronymic: str, achievement: dict[list[int]]):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.achievement = achievement
        sum_key_0 = 0
        sum_key_1 = 0
        count = 0
        for key in achievement:
            count += 1
            sum_key_0 += achievement[key][0]
            sum_key_1 += achievement[key][1]
            print(key, achievement[key][0], achievement[key][1])
        sum_key_0 = sum_key_0 / count
        sum_key_1 = sum_key_1 / count

    def __repr__(self):
        return f'Student(surname={self.surname},name={self.name},patronymic={self.patronymic},achievement={self.achievement})'


if __name__ == '__main__':
    std1 = Student('Иванов', 'Иван', 'Иванович', {'123': [5, 50]})
    std2 = Student('Иванов', 'Иван', 'Иванович', {'algebra': [4, 40]})
    std3 = Student('Иванов', 'Иван', 'Иванович', {'history': [3, 60]})
    print(f'{std1 = }')
