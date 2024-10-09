from googletrans import Translator, LANGUAGES


translator = Translator()

def TransLate(str, lang):
    try:
        translated = translator.translate(str, dest=lang)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(txt):
    try:
        detected = translator.detect(txt)
        return f"Detected(lang={detected.lang}, confidence={detected.confidence})"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang):
    lang_lower = lang.lower()
    for code, name in LANGUAGES.items():
        if lang_lower == code or lang_lower == name:
            return code if lang_lower == name else name
    return "Unknown language"

txt = "Доброго дня. Як справи?"
lang = "en"
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))
