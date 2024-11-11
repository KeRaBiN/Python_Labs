from googletrans import Translator, LANGUAGES

translator = Translator()


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return f"Мова: {detected.lang}, Коефіцієнт довіри: {detected.confidence}"
    except Exception as e:
        return f"Помилка: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        if lang in LANGUAGES.values():
            for code, name in LANGUAGES.items():
                if name == lang:
                    return code
        elif lang in LANGUAGES.keys():
            return LANGUAGES[lang]
        else:
            return "Помилка: мову не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        table = "N  Language    ISO-639 code    Text\n" + "-" * 50 + "\n"
        for i, (code, language) in enumerate(LANGUAGES.items(), 1):
            translated_text = ""
            if text:
                translated_text = TransLate(text, "auto", code)
            table += f"{i:<4} {language:<12} {code:<15} {translated_text}\n"

        if out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(table)
            return "Ok"
        else:
            print(table)
            return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"
