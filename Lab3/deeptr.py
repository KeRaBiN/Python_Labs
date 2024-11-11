from translate_modules.deep_trans import TransLate, LangDetect, CodeLang, LanguageList

print(TransLate("Hello, world!", "en", "uk"))

print(LangDetect("Привіт, світ!", "all"))

print(CodeLang("uk"))

print(LanguageList("screen", "Добрий день"))
