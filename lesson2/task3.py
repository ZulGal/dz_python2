# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

str_first = input("Введите первую дробь в виде a/b : ")
list_first = str_first.split('/')
str_second = input("Введите вторую дробь в виде a/b : ")
list_second = str_second.split('/')

for i in range(2):
    list_first[i] = int(list_first[i])
    list_second[i] = int(list_second[i])

list_sum = [0,0]
list_sum[0] = list_first[0] * list_second[1] + list_second[0] * list_first[1]
list_sum[1] = list_first[1] * list_second[1]
j=2
temp = min(list_sum)
while (j < temp**0.5):
    while (list_sum[0] % j == 0) and (list_sum[1] % j == 0):
        list_sum[0] = list_sum[0] // j
        list_sum[1] = list_sum[1] // j
    j +=1
result_sum = f"{list_sum[0]}/{list_sum[1]}"

list_prod = [0,0]
list_prod[0] = list_first[0] * list_second[0]
list_prod[1] = list_first[1] * list_second[1]
j=2

temp = min(list_prod)
while (j < temp**0.5):
    while (list_prod[0] % j == 0) and (list_prod[1] % j == 0):
        list_prod[0] = list_prod[0] // j
        list_prod[1] = list_prod[1] // j
    j +=1
result_prod = f"{list_prod[0]}/{list_prod[1]}"

f1 = fractions.Fraction(list_first[0],list_first[1])
f2 = fractions.Fraction(list_second[0],list_second[1])
print(result_sum, f1+f2)
print(result_prod, f1*f2)