"""Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу."""
from random import randint

classes = ['4a', '2b', '6c', '8']
school = []
for x in classes:
    marks = []
    for m in range(randint(1, 10)):
        marks.append(randint(1, 5))
    school.append({'school_class': x, 'scores': marks})

print("Оценки по школе:")
for clas in school:
    print("В классе номер {0} оценки {1}".format(clas['school_class'], clas['scores']))

school_total_scores = []
for cl in school:
    print('Средний бал по классу {0} равен {1}'.format(cl['school_class'], int(sum(cl['scores']) / len(cl['scores']))))
    school_total_scores = school_total_scores + cl['scores']
print("Средний балл по школе равен {0}".format(int(sum(school_total_scores) / len(school_total_scores))))