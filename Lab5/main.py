import string
import re


def sort_words(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    words = cleaned_text.split()

    uk_words = [word for word in words if all('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)]
    en_words = [word for word in words if all(char in string.ascii_letters for char in word)]

    uk_words.sort()
    en_words.sort()

    return uk_words, en_words


try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        full_text = file.read()

        sentences = re.split(r'[.!?]', full_text)
        first_sentence = sentences[0].strip() if sentences else ''

        print("Перше речення:", first_sentence)

        uk_words, en_words = sort_words(full_text)

        print("\nСлова українською мовою (в алфавітному порядку):")
        print(uk_words)
        print(f"Кількість українських слів: {len(uk_words)}")

        print("\nСлова англійською мовою (в алфавітному порядку):")
        print(en_words)
        print(f"Кількість англійських слів: {len(en_words)}")

        print(f"Загальна кількість слів: {len(uk_words) + len(en_words)}")

except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except Exception as e:
    print(f"Сталася помилка: {e}")
