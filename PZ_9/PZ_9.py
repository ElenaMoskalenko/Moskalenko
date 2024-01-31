# Используя словарь посчитать количество уникальных слов в заданном
# предложении «Изучаем язык Питон». Вывести на экран каждую пару
# «ключ:значение».

sentence = "Изучаем язык Питон"

words = sentence.split()

unique_word_count = {}

for word in words:
    if word in unique_word_count:
        unique_word_count[word] += 1
    else:
        unique_word_count[word] = 1

for word, count in unique_word_count.items():
    print(f"{word}:{count}")