import json
from translate_modules.deep_trans import TransLate


def read_configuration():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def process_text_file(config):
    filename = config["filename"]
    target_language = config["target_language"]
    output = config["output"]
    max_chars = config["max_chars"]
    max_words = config["max_words"]
    max_sentences = config["max_sentences"]

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

            num_chars = len(text)
            num_words = len(text.split())
            num_sentences = text.count('.') + text.count('!') + text.count('?')

            print(f"Файл: {filename}")
            print(f"Кількість символів: {num_chars}")
            print(f"Кількість слів: {num_words}")
            print(f"Кількість речень: {num_sentences}")

            if num_chars > max_chars or num_words > max_words or num_sentences > max_sentences:
                text = ' '.join(text.split()[:max_words])

            translated_text = TransLate(text, 'auto', target_language)

            if output == "screen":
                print(f"Перекладений текст на {target_language}:\n{translated_text}")
            elif output == "file":
                output_filename = f"{filename.split('.')[0]}_{target_language}.txt"
                with open(output_filename, "w", encoding="utf-8") as out_file:
                    out_file.write(translated_text)
                print("Ok")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    config = read_configuration()
    process_text_file(config)
