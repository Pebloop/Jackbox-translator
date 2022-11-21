from __future__ import annotations

import json

import PySimpleGUI as sg

from src.data.game import Game
from src.data.games.jackbox2.jackbox2 import Jackbox2
from src.data.jackgame import JackGame


class Project:
    _name: str = "myProject"
    _language: str = "en"
    _path: str = ""
    _game: JackGame = JackGame.UNKNOWN
    _translation: Game

    def __init__(self, name: str, language: str, path: str, game: JackGame):
        """Project class constructor

        This method is used to initialize the project class.
        :param name: The name of the project.
        :param language: The language of the project.
        :param path: The path of the project.
        :param game: The game of the project.
        """
        self._name = name
        self._language = language
        self._path = path
        self._game = game
        self._file = ProjectFile(self)
        self._translation = self._instantiate_game()

    def _instantiate_game(self) -> Game:
        """Instantiate the game.

        This method is used to instantiate the game.
        :return: The game.
        """
        if self._game == JackGame.JACKBOX1:
            sg.Popup("Jackbox 1 not yet Implemented")
        elif self._game == JackGame.JACKBOX2:
            return Jackbox2()
        elif self._game == JackGame.JACKBOX3:
            sg.Popup("Jackbox 3 not yet Implemented")
        elif self._game == JackGame.JACKBOX4:
            sg.Popup("Jackbox 4 not yet Implemented")
        elif self._game == JackGame.JACKBOX5:
            sg.Popup("Jackbox 5 not yet Implemented")
        elif self._game == JackGame.JACKBOX6:
            sg.Popup("Jackbox 6 not yet Implemented")
        elif self._game == JackGame.JACKBOX7:
            sg.Popup("Jackbox 7 not yet Implemented")
        elif self._game == JackGame.JACKBOX8:
            sg.Popup("Jackbox 8 not yet Implemented")
        elif self._game == JackGame.JACKBOX9:
            sg.Popup("Jackbox 9 not yet Implemented")
        return Game(JackGame.UNKNOWN)

    def get_name(self) -> str:
        """Get the name of the project.

        This method is used to get the name of the project.
        :return: The name of the project.
        """
        return self._name

    def get_language(self) -> str:
        """Get the language of the project.

        This method is used to get the language of the project.
        :return: The language of the project.
        """
        return self._language

    def get_path(self) -> str:
        """Get the path of the project.

        This method is used to get the path of the project.
        :return: The path of the project.
        """
        return self._path

    def get_game(self) -> JackGame:
        """Get the game of the project.

        This method is used to get the game of the project.
        :return: The game of the project.
        """
        return self._game

    def create(self):
        """Create the project.

        This method is used to create the project.
        """
        self._file.save()


class ProjectFile:
    NAME = "name"
    GAME = "game"
    LANGUAGE = "language"
    LOCATION = "location"
    TRANSLATION = "translation"

    def __init__(self, project: Project):
        self._project = project
        self._file = { }
        self._update_file(name = self._project.get_name(),
                          language = self._project.get_language(),
                          game = self._project.get_game(),
                          location = self._project.get_path())

    def load(self) -> bool:
        try:
            with open("./save/projects/" + self._project.get_name(), "r") as file:
                self._file = json.load(file)
                file.close()
            self._update_file()
            return True
        except FileNotFoundError:
            self._update_file()
            return False

    def save(self):
        with open("./save/projects/" + self._project.get_name(), "w") as file:
            json.dump(self._file, file)
            file.close()

    def _update_file(self, name: str = None, language: str = None, game: JackGame = None, location: str = None,
                     translation: Game = None):
        self._file = {
                ProjectFile.NAME       : name or self._file.get(ProjectFile.NAME) or "myProject",
                ProjectFile.LANGUAGE   : language or self._file.get(ProjectFile.LANGUAGE) or 'EN',
                ProjectFile.GAME       : str(game) or self._file.get(ProjectFile.GAME) or str(JackGame.UNKNOWN),
                ProjectFile.LOCATION   : location or self._file.get(ProjectFile.LOCATION) or "",
                ProjectFile.TRANSLATION: translation or self._file.get(ProjectFile.TRANSLATION) or []
                }
