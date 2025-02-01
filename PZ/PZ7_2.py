#Дана строка, состоящая из русских слов, разделённых пробелами.
#Найти длину самого короткого слова
input_string = input("Введите строку: ")
words = input_string.split()

if words:
    shortest_word_length = min(len(word) for word in words)
    print(f"Длина самого короткого слова: {shortest_word_length}")
else:
    print("Строка не содержит слов.")