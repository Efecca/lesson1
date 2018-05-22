# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Петя'},
]
from collections import Counter
cnt = Counter(person['first_name'] for person in students)
for value, count in cnt.items():
    print(value, count)
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Оля'},
	{'first_name': 'Оля'}
]
# Пример вывода:
# Самое частое имя среди учеников: Маша
cnt = Counter(person['first_name'] for person in students)
max_cnt = cnt.most_common(1)[0][1]
name_list = [val[0] for val in cnt.items() if val[1] == max_cnt]
print('\n'.join('Самое частое имя среди учеников: {}'.format(name) for name in name_list))

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
	[  # это – первый класс
		{'first_name': 'Вася'},
		{'first_name': 'Вася'},
	],
	[  # это – второй класс
		{'first_name': 'Маша'},
		{'first_name': 'Маша'},
		{'first_name': 'Оля'},
        {'first_name': 'Оля'}
	]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
for index, students in enumerate(school_students):
    cnt = Counter(person['first_name'] for person in students)
    max_cnt = cnt.most_common(1)[0][1]
    name_list = [val[0] for val in cnt.items() if val[1] == max_cnt]
    print('\n'.join('Самое частое имя  классе {}: {}'.format(index+1,name) for name in name_list))

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
	'Маша': False,
	'Оля': False,
	'Олег': True,
	'Миша': True,
}
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
for school_class in school:
    gender={'boys':0,'girls':0}
    for student in school_class['students']:
        if student['first_name'] not in is_male:
            raise ValueError('Gender was not specified for student: {}'.format(student['first_name'] ))
        if is_male[student['first_name']]:
            gender['boys']+=1 
        else:
            gender['girls']+=1
    print('В классе {} {} девочки и {} мальчика.'.format(school_class['class'], str(gender['girls']),str(gender['boys'])))


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
	'Маша': False,
	'Оля': False,
	'Олег': True,
	'Миша': True,
}
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
school_genders = [{'class': school_class['class'], 'boys':sum(is_male[student['first_name']] for student in school_class['students'])} for school_class in school]
max_boys=max(school_genders, key=lambda x: x['boys'])
#Здесь используется неявная логика, что все, кто не мальчик, тот девочка, что может не сработать в случае гермафродитов и лиц неопределенного пола
max_girls=min(school_genders, key=lambda x: x['boys'])
print('Больше всего мальчиков в классе {}'.format(str(max_boys['class'])))
print('Больше всего девочек в классе {}'.format(str(max_girls['class'])))