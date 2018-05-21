#Создайте словарь weather с ключами city, temperature, wind и значениями Москва, 20, восточный
weather = {"city":"Москва", "temperature":20, "wind":"Восточный"}

#Выведите на экран значение по ключу city
print(weather["city"])

#Измените значение температуры и выведите на экран новое значение
weather["temperature"]= -20
print(weather["temperature"])

#Посчитайте количество элементов словаря
print('Количество элементов словаря: '+ str(len(weather)))

#Проверьте, есть ли в словаре ключ country
print('Есть' if "country" in weather else 'Нет')

#Добавьте в словарь элемент date со значением '27.05.2017'
weather['date'] = '27.05.2017'

#Создайте список, добавьте туда три словаря с погодой за разные даты при помощи append()
from datetime import datetime  
from datetime import timedelta  
now = datetime.now()

dict_list = []
dict_list.append({"city":"Москва", "temperature":20, "wind":"ЮВ", "date":str(now)[:10]})
dict_list.append({"city":"Ахшабад", "temperature":36, "wind":"СЗ", "date":str(now-timedelta(days=30))[:10]}) #здесь нет dateadd(), ну как так :(
dict_list.append({"city":"Токио", "temperature":10, "wind":"ЮЮЗ", "date":str(now-timedelta(days=-30))[:10]})
print(dict_list)