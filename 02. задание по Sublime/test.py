#словарь, в котором ключи - имена людей, а значения - словари с ключами city, temperature, wind
weather = {"Иванов":{"city":"London", "temperature":15, "wind":"NW"},"Петров":{"city":"Chikago", "temperature":20, "wind":"W"},"Сидоров":{"city":"Osaka", "temperature":25, "wind":"E"}}
#Спрашивает у пользователя имя, используя функцию input
name = input("Enter name: ")
#Выводит город, температуру и погоду по введенному имени
print(weather[name] if name in weather else 'Wrong choice')
#Что будет, если ввести несуществующее имя?
#Wrong choice