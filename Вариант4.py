# Получение строки от пользователя
string = input("Введите строку: ")

# Подсчет количества символов в строке
length = len(string)

# Подсчет количества замен
count = string.count('а')

# Замена всех букв "а" на букву "о"
string = string.replace('а', 'о')

# Вывод модифицированной строки и количества замен
print("Модифицированная строка:", string)
print("Количество замен:", count)
print("Количество символов в строке:", length)
