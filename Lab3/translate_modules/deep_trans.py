from googletrans import Translator
from googletrans import LANGUAGES

translator = Translator()


def TransLate(text: str, src: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return f"{detected.lang}, {detected.confidence}"
    except Exception as e:
        return f"Помилка: {e}"


def CodeLang(lang: str) -> str:
    try:
        if lang in LANGUAGES.values():
            return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
        elif lang in LANGUAGES:
            return LANGUAGES[lang]
        else:
            return "Помилка: Невідомий код або назва мови"
    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        lines = []
        header = "N  Language       ISO-639 code  Text\n" + "-" * 60
        lines.append(header)

        for i, (code, language) in enumerate(LANGUAGES.items(), 1):
            translated_text = translator.translate(text, dest=code).text if text else ""
            lines.append(f"{i:<3} {language:<15} {code:<12} {translated_text}")

        result = "\n".join(lines)
        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(result)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
