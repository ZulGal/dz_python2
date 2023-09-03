# Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint

class Game:
    def __init__(self,down, up,limit):
        self.down = down
        self.up = up
        self.limit = limit

    def search_number(self):
        self.number = randint(self.down,self.up)
        print(self.number)
        count = 0
        answer = 0
        while count < self.limit and self.number != answer:
            answer = int(input(f"Угадайте число в промежутке ({self.down},{self.up}) за {self.limit-count} попыток: "))
            count +=1
            if answer > self.number:
                print("Ваше число больше искомого")
            elif answer < self.number:
                print("Ваше число меньше искомого")
        if self.number == answer:
            print("Угадали")
            return True
        else:
            return(False)

if __name__ == '__main__':
    g = Game(0,100,10)
    g.search_number()
   