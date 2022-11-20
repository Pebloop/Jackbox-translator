import json
import os
from typing import List


class LanguageManager:
    languages: List[str] = []
    current_language: int = 0
    current_language_dict: dict = { }

    def __init__(self, language: str):
        self.load_languages()
        self.load_language(language)

    def load_languages(self):

        languages_dir_content = os.listdir("languages/")
        languages_dir_content = list((x for x in languages_dir_content if x.endswith('.json')))
        self.languages = list(map(lambda x: x.split('.')[0], languages_dir_content))

        self.load_language(self.languages[0])

    def load_language(self, language: str):

        try:
            self.current_language = self.languages.index(language)
        except:
            print("Could not load new language")
            return

        language_file = open("languages/" + self.languages[self.current_language] + ".json", 'r')
        self.current_language_dict = json.load(language_file)

    def get_text(self, key: str):
        if len(self.languages) == 0:
            self.load_languages()
        text = self.current_language_dict.get(key)
        return text

    def get_current_language(self):
        return self.languages[self.current_language]
