import json
from typing import List

from src.data.projects.metaproject import MetaProject


class SaveFile:
    PROJECTS = "projects"
    LANGUAGE = "language"

    _file: dict

    def __init__(self):
        self._projects: List[MetaProject] = []
        self._language = None
        self._file = { }
        self.load()

    def _update_file(self, projects: List[MetaProject] = None, language: str = None):
        self._file = {
                SaveFile.PROJECTS: self.meta_to_dict(projects) if projects is not None else
                self._file.get(SaveFile.PROJECTS) or [],
                SaveFile.LANGUAGE: language or self._file.get(SaveFile.LANGUAGE) or 'EN'
                }

    def meta_to_dict(self, meta: List[MetaProject]) -> list:
        projects = []
        if meta is not None:
            for project in meta:
                projects.append(project.to_json())
        return projects

    def load(self) -> bool:
        try:
            with open("./save/save", "r") as file:
                self._file = json.load(file)
                self._projects = [MetaProject(save_dict = meta) for meta in self._file.get(SaveFile.PROJECTS)] or []
                self._language = self._file.get(SaveFile.LANGUAGE) or 'EN'
                file.close()
            self._update_file()
            return True
        except FileNotFoundError:
            self._update_file()
            return False

    def save(self):
        with open("./save/save", "w") as file:
            self._update_file(self._projects, self._language)
            json.dump(self._file, file)
            file.close()

    def get_projects(self) -> List[MetaProject]:
        return self._projects

    def get_language(self):
        return self._language

    def set_language(self, language: str):
        self._language = language
