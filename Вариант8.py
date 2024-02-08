# Получение строки от пользователя
string = input("Введите строку: ")

# Проверка, заканчивается ли строка точкой
if string.endswith('.'):
    # Разбиение строки на слова по пробелам
    words = string[:-1].split()  # исключаем точку из строки и разбиваем на слова
    # Подсчет количества слов в строке
    word_count = len(words)
    # Вывод количества слов в строке
    print("Количество слов в строке:", word_count)
else:
    print("Ошибка: Строка не заканчивается точкой.")
