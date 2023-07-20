# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю INITIAL_AMOUNT
# ✔ Допустимые действия: пополнить, снять, выйти top_up withdraw exit
# ✔ Сумма пополнения и снятия кратны 50 у.е. SUM_OPERATION
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.PERCENT_WITHDRAW MIN_WITHDRAW MAX_WITHDRAW
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% COUNT_OPERATIONS_PERCENT_ACCRUAL PERCENT_ACCRUAL
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой LIMIT_WEALTH_TAX PERCENT_WEALTH_TAX
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import decimal

INITIAL_AMOUNT = 0
SUM_OPERATION = 50
PERCENT_WITHDRAW = decimal.Decimal(1.5)
MIN_WITHDRAW = 30
MAX_WITHDRAW = 600
COUNT_OPERATIONS_PERCENT_ACCRUAL = 3
PERCENT_ACCRUAL = decimal.Decimal(3)
LIMIT_WEALTH_TAX = 5000000
PERCENT_WEALTH_TAX = decimal.Decimal(10)
decimal.getcontext().prec = 10
sum = decimal.Decimal(0)
count_accrual = 0;
print(f"Баланс: {sum}")
def wealth_tax():
    global sum
    if sum > LIMIT_WEALTH_TAX:
        sum *= 1 - PERCENT_WEALTH_TAX / 100
    print(f"Баланс: {sum}")
def top_up():
    global sum
    global count_accrual
    sum_operation = INITIAL_AMOUNT + 1
    while sum_operation % SUM_OPERATION != 0:
        sum_operation = int(input(f"Введите сумму пополнения (кратно {SUM_OPERATION}): "))
    sum += sum_operation
    print(f"Баланс: {sum}")
    count_accrual +=1
    if count_accrual > COUNT_OPERATIONS_PERCENT_ACCRUAL:
        sum *= 1 + PERCENT_ACCRUAL/100
        sum_print = round(sum,2)
        print(f"Баланс: {sum_print}")

def withdraw():
    global sum
    global count_accrual
    sum_operation = INITIAL_AMOUNT + 1
    while sum_operation % SUM_OPERATION != 0 or sum_operation < MIN_WITHDRAW or sum_operation > MAX_WITHDRAW:
        sum_operation = int(input(
            f"Введите сумму снятия (кратно {SUM_OPERATION} не меньше {MIN_WITHDRAW} и не больше {MAX_WITHDRAW} или остатка на счете = {sum}: "))
    sum -= sum_operation
    print(f"Баланс: {sum}")

    count_accrual += 1
    if count_accrual > COUNT_OPERATIONS_PERCENT_ACCRUAL:
        sum *= 1 + PERCENT_ACCRUAL / 100
        count_accrual = 0
        print(f"Баланс: {sum}")

main_instruction = 'Введите команду top (пополнить), withdraw (снять), exit (выйти):   '
command = ''

while command != 'exit':
    command = input(main_instruction)
    if command == 'top':
        wealth_tax()
        top_up()
    elif command == 'withdraw':
        wealth_tax()
        withdraw()

