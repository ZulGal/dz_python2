# Задача 2. Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self, name: str, age: int, color: str, breed: str, is_domestic: bool):
        super().__init__(name, age)
        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'{self.name} {self.color} {self.breed} домашняя'
        return f'{self.name} {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self, age: int, name: str, number_heads: int = 2):
        super().__init__(name, age)
        self.number_heads = number_heads

    def __str_(self):
        return f'kotopes - number_heads: {self.number_heads} Возраст: {self.age}'


class Fish(Animal):
    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.name:
            return f'морская'
        return f'пресноводная'


class Factory:
    def __init__(self, class_type, name, age, *args, **kwargs):
        self.class_type = class_type
        self.name = name
        self.age = age

    def get_inst(self):
        MyClassInstance = globals()[self.class_type]()
        return MyClassInstance

    def __str__(self) -> str:
        return f'{self.name} {self.age}'


if __name__ == '__main__':
    f1 = Factory('Dog', 'Бобик', 3, 'рыжий', 'спаниель', True)
    print(f1)
    f2 = Factory('Fish', 'Дори', 1, True, 0.5)
    print(f2)
    f3 = Factory('Kotopes', 3, 'Kotopes', 3)
    print(f3)
