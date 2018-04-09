import requests
import os


def open_file(name_file):
    """Передаем имя файла, определяет абс. путь, открывает файл, читаем данные, из названия файла берем язык с
    которго переводим, формурием путь для файла результата перевода
    Фун-ция возвраешт текс файла, язык и путь файла результата"""

    current_dir = os.path.dirname(os.path.abspath(name_file))
    path_file = os.path.join(current_dir, name_file)

    with open(path_file) as file:
        data_text = file.read()

    from_lang = name_file.lower().split('.')[0]
    file_translate = os.path.join(current_dir, 'Result translate {}-ru.txt'.format(from_lang))

    return data_text, from_lang, file_translate


def translate_it(text, from_lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': '{}-ru'.format(from_lang),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def write_result(file_translate, text_translate):
    """Функция записи перевода в файл
    принимает путь к файлу и результат первевода"""

    with open(file_translate, 'w') as file:
        file.write(text_translate)


def main():
    """Указываем список файлов для перевода, проходимся циклом по всем файлам,
    вызываем функцию open_file(file) и присавимваем значания ТЕКСТ, ЯЗЫК, ПУТЬ К РЕЗУЛЬТАТУ
    вызываем функцию translate_it передав текст и язык
    вызываем функцию записи в файл передав результат перевода и путь к файду"""

    list_file = ['DE.txt', 'ES.txt', 'FR.txt']
    for file in list_file:
        data_text, from_lang, file_translate = open_file(file)
        text_translate = translate_it(data_text, from_lang)
        write_result(file_translate, text_translate)


main()
