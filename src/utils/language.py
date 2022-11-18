import json
import os
from typing import List

languages: List[str] = []
current_language: int = 0
current_language_dict: dict = {}


def load_languages():
    global languages

    languages_dir_content = os.listdir("languages/")
    languages_dir_content = list((x for x in languages_dir_content if x.endswith('.json')))
    languages = list(map(lambda x: x.split('.')[0], languages_dir_content))

    load_language(languages[0])


def load_language(language: str):
    global current_language_dict

    try:
        current_language = languages.index(language)
    except:
        print("Could not load new language")
        return

    language_file = open("languages/" + languages[current_language] + ".json", 'r')
    current_language_dict = json.load(language_file)


def get_text(key: str):
    if len(languages) == 0:
        load_languages()
    text = current_language_dict.get(key)
    return text


def get_current_language():
    return languages[current_language]
