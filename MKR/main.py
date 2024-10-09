import os
import json
from googletrans import Translator, LANGUAGES


FILENAME = "MyData.dat"

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
    return None

def read_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                data = json.load(file)
            return data
        except (json.JSONDecodeError, KeyError):
            print("Файл MyData пошкоджений або некоректний.")
            return None
    return None

def write_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file)
    print(f"Дані збережено в файл {FILENAME}")

def get_user_input():
    try:
        x, y = map(float, input("Введіть координати точки А(x,y): ").split())
        r = float(input("Введіть радіус першого кола r: "))
        R = float(input("Введіть радіус другого кола R: "))
        language = input("Введіть мову інтерфейсу: ").strip().lower()
        if CodeLang(language) is None:
            print("Невідома мова, за замовчуванням обрана українська.")
            language = 'uk'
        return {'x': x, 'y': y, 'r': r, 'R': R, 'language': language}
    except ValueError:
        print("Некоректні дані. Будь ласка, спробуйте ще раз.")
        return get_user_input()

def is_point_in_torus(x, y, r, R):
    distance = (x**2 + y**2)**0.5
    return r <= distance <= R


data = read_data()
if data is None:
    data = get_user_input()
    write_data(data)
    exit()

language = data.get('language')
print(CodeLang(language))

x, y = data['x'], data['y']
r, R = data['r'], data['R']

distance = (x ** 2 + y ** 2) ** 0.5
print(f"{TransLate('Координати точки А(x,y)', language)}: {x} {y}")
print(f"{TransLate('Радіус першого кола r', language)}: {r}")
print(f"{TransLate('Радіус другого кола R', language)}: {R}")
print(f"{TransLate('Відстань до точки A', language)}: {distance:.2f}")

if is_point_in_torus(x, y, r, R):
    print(f"{TransLate('Точка A знаходиться всередині тора', language)}.")
else:
    print(f"{TransLate('Точка A не знаходиться всередині тора', language)}.")
