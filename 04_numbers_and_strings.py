# a = 2
# b = ???
# print(a + b)  # надо, чтобы выводилось 6.5
a=2
b=6.5-2 #раз надо, то выведем
print(a + b)

# v = input('Введите число от 1 до 10: ')
# print(???)  
# надо, чтобы выводилось число на 10 больше, чем введённое
v = input('Введите число от 1 до 10: ')
try:
	print( int(v)+10 if int(v) < 10  else 'ну нет так нет')
except ValueError:
	print('Видимо, это было не число...')

# name = input('Введите ваше имя: ')
# print(???)  # Привет, Артём! Как дела?
name = input('Введите ваше имя: ')
print('Привет, {}! Как дела?'.format(name))

# float('1')  - 1.0
# int('2.5')  - ValueError: invalid literal for int() with base 10: '2.5'
# bool(1) - True
# bool('')  - False
# bool(0)  - False