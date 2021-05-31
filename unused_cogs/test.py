from translate import Translator

import json


with open('databases/iso639-1/db_languages.json', encoding='utf-8') as f:
    data = f.read()
    lang = json.loads(data)


def languageTranslate(language):
    if language in lang:
        codename = lang[language]['codename']
        return codename
    else:
        pass


while True:
    for language in lang:
        try:
            translator = Translator(
                from_lang='en', to_lang=lang[language]['codename']
            )
            translation = translator.translate('hello')
            print(translation)
        except StopIteration:
            continue
