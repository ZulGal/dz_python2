# Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

class Calendar:
    def __init__(self, data):
        self.data = data

    def data_is_valid(self):
        dd, mm, yyyy = (self.data.split('.'))
        dd_, mm_, yyyy_ = int(dd), int(mm), int(yyyy)
        if yyyy_ >= 1 and yyyy_ <= 9999 and mm_ >= 1 and mm_ <= 12 and (
                (is_leap(yyyy_) and dd_ <= 29) or (not is_leap(yyyy_) and dd_ <= 28)):
            return True
        else:
            return False


def is_leap(year_):
    LEAP_MAIN = 4
    LEAP_EXCLUDE = 100
    LEAP_ADDITION = 400

    if year_ % LEAP_MAIN == 0 and year_ % LEAP_EXCLUDE != 0 or year_ % LEAP_ADDITION == 0:
        return True
    else:
        return False


c = Calendar('29.02.2000')
print(c.data_is_valid())
