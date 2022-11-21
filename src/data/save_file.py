import json


class SaveFile:
    PROJECTS = "projects"
    LANGUAGE = "language"

    _file: dict

    def __init__(self):
        self._file = { }
        self.load()

    def _update_file(self, projects: list = None, language: str = None):
        self._file = {
                SaveFile.PROJECTS: projects or self._file.get(SaveFile.PROJECTS) or [],
                SaveFile.LANGUAGE: language or self._file.get(SaveFile.LANGUAGE) or 'EN'
                }

    def load(self) -> bool:
        try:
            with open("./save/save", "r") as file:
                self._file = json.load(file)
                file.close()
            self._update_file()
            return True
        except FileNotFoundError:
            self._update_file()
            return False

    def save(self):
        with open("./save/save", "w") as file:
            json.dump(self._file, file)
            file.close()

    def get_projects(self) -> list:
        return self._file.get(SaveFile.PROJECTS)

    def get_language(self):
        return self._file.get(SaveFile.LANGUAGE)

    def set_language(self, language: str):
        self._file.update(language = language)
