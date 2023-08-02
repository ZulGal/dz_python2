# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibo(n: int):
    fib1 = 1
    fib2 = 1
    yield 1
    yield 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        yield fib2


print([i for i in fibo(10)])
