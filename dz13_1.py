# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class MyException(Exception):
    pass

class MyExceptionValueNegativeError(MyException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Сторона прямоугольника не должна быть отрицательной:{self.value}'


class Rectangle:

    def __init__(self,length: float, width: float= None) -> None:
        self.__length = length
        if width:
            self.__width = width
        else:
            self.__width = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value


if __name__ == '__main__':
    r1 = Rectangle(0,0)

    a = 22
    if a < 0 :
        raise MyExceptionValueNegativeError(a)
    r1.length = a
    print(r1.length)
    b = -44
    if b < 0 :
        raise MyExceptionValueNegativeError(b)
    r1.width = b
    print(r1.width)

