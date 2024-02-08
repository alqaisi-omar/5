# Получение строки от пользователя
string = input("Введите строку: ")

# Подсчет самой длинной последовательности букв "н"
max_sequence_length = 0
current_sequence_length = 0

for char in string:
    if char == 'н':
        current_sequence_length += 1
        max_sequence_length = max(max_sequence_length, current_sequence_length)
    else:
        current_sequence_length = 0

# Замена восклицательных знаков точками
modified_string = string.replace('!', '.')

# Вывод результата
print("Самая длинная последовательность букв 'н':", max_sequence_length)
print("Модифицированная строка:", modified_string)
