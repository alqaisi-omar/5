# Получение строки от пользователя
string = input("Введите строку: ")

# Разделение строки на слова
words = string.split()

# Вывод слов, оканчивающихся на букву "я"
print("Слова, оканчивающиеся на букву 'я':")
for word in words:
    if word.endswith('я'):
        print(word)
