# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
HEX_DIV = 16
num = int(input("Введите целое число: "))
dict_hex = {0: '0',1: '1',2: '2',3: '3',4: '4',5: '5',6: "6",7: '7',8: '8',9: '9',10: 'A',11: 'B',12: 'C', 13: 'D',14: 'E',15: 'F'}
print(dict_hex)
process_num = num
res = ''
while process_num > 0:
    for k, v in dict_hex.items():
        if process_num % HEX_DIV == k:
            res += v
    process_num //= HEX_DIV

res = res [::-1]
print(res, hex(num))