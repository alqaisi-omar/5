# Получение текста от пользователя
text = input("Введите текст: ")
# Получение заданного слова от пользователя
word = input("Введите слово для поиска: ")

# Разбиение текста на слова с использованием пробела в качестве разделителя
words = text.split()

# Подсчет количества вхождений заданного слова в тексте
count = words.count(word)

# Вывод результата
print("Слово", word, "встречается в тексте", count, "раз(а).")
