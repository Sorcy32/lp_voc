"""Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1."""


ls = []
for x in range(10):
    x += 1
    ls.append(x)
    print(x)


