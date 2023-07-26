# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
my_list = [1, 2, 3, 1, 2, 4, 5]
result = []
for i in my_list:
    while (my_list.count(i) > 1):
        result.append(i)
        my_list.remove(i)
print(result)
