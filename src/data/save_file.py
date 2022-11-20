import json


class SaveFile:
    _file: dict = {
            "projects": []
            }

    def __init__(self):
        self.load()

    def load(self) -> bool:
        try:
            with open("./save/save", "r") as file:
                self._file = json.load(file)
                return True
        except FileNotFoundError:
            return False

    def save(self):
        with open("./save/save", "w") as file:
            json.dump(self._file, file)

    def get_projects(self) -> list:
        return self._file.get("projects")
