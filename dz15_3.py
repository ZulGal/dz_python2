# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование
# ошибок и полезной информации. Также реализуйте возможность запуска
# из командной строки с передачей параметров.

# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

import argparse
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename = "log_dz15_1.log", encoding = "utf-8", level=logging.ERROR)
def correct_input(text: str):
    while True:
        text = input('Введите число: ')
        try:
            num = float(text)
            break
        except ValueError as e:
            logger.error (f'temp={text} {e}')
            print(f'Вы ввели не число: {e}')

    return num
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Correct int value')
    parser.add_argument('param', metavar='text', type=int,
                    nargs=1,
                    help='enter text')
    args = parser.parse_args()
    print(correct_input(*args.param))





