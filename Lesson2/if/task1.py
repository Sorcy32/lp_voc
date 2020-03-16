"""Написать функцию, которая принимает на вход две строки
Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
Если строки одинаковые, вернуть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты"""


def func(str_a, str_b):
    if type(str_a) != str or type(str_b) != str:
        return 0
    elif str_a == str_b:
        return 1
    elif str_a != str_b:
        if len(str_a) > len(str_b):
            return 2
        elif str_b == 'Learn':
            return 3


if __name__ == "__main__":
    print(func('The line', 2))
    print(func('The line', 'The line'))
    print(func('The line', 'Learn'))
    print(func('The line', 'The long line'))
    print(func('The long line', 'The line'))
