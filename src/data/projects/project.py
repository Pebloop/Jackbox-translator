from __future__ import annotations

import json

from src.data.games.game import Game
from src.data.games.gameclasses import GAME_CLASSES
from src.data.games.gamelist import GameList


class Project:
    _name: str = "myProject"
    _language: str = "en"
    _path: str = ""
    _game: GameList = GameList.UNKNOWN
    _data: Game = Game()

    def __init__(self, name: str, language: str, path: str, game: GameList):
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
        self._data = self._instantiate_game()

    def _instantiate_game(self) -> Game:
        """Instantiate the game.

        This method is used to instantiate the game.
        :return: The game.
        """
        for game in GAME_CLASSES:
            if game.get_game() == self._game:
                return game()

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

    def get_game(self) -> GameList:
        """Get the game of the project.

        This method is used to get the game of the project.
        :return: The game of the project.
        """
        return self._game

    def get_data(self) -> Game:
        """Get the data of the project.

        This method is used to get the data of the project.
        :return: The data of the project.
        """
        return self._data

    def create(self):
        """Create the project.

        This method is used to create the project.
        """
        self._file.save()

    def load(self):
        """Load the project.

        This method is used to load the project.
        """
        self._file.load()
        self._language = self._file.get_language()
        self._path = self._file.get_location()
        self._game = self._file.get_game()
        self._data = self._file.get_data().to_game(self._game)
        print("project loaded !")

    @classmethod
    def load_project(cls, name: str) -> Project:
        project = Project(name, "EN", "", GameList.UNKNOWN)
        project.load()
        return project


class ProjectFile:
    NAME = "name"
    GAME = "game"
    LANGUAGE = "language"
    LOCATION = "location"
    DATA = "data"

    def __init__(self, project: Project):
        self._project = project
        self._file = { }
        self._update_file(name = self._project.get_name(),
                          language = self._project.get_language(),
                          game = self._project.get_game(),
                          location = self._project.get_path(),
                          data = GameFile(self._project.get_data())
                          )

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

    def _update_file(self, name: str = None, language: str = None, game: GameList = None, location: str = None,
                     data: GameFile = None):

        self._file = {
                ProjectFile.NAME    : name or self._file.get(ProjectFile.NAME) or "myProject",
                ProjectFile.LANGUAGE: language or self._file.get(ProjectFile.LANGUAGE) or 'EN',
                ProjectFile.GAME    : game.value if game is not None else self._file.get(ProjectFile.GAME) or str(
                        GameList.UNKNOWN),
                ProjectFile.LOCATION: location or self._file.get(ProjectFile.LOCATION) or "",
                ProjectFile.DATA    : data.to_json() if data is not None else self._file.get(ProjectFile.DATA) or { }
                }

    def get_name(self) -> str:
        return self._file.get(ProjectFile.NAME)

    def get_language(self) -> str:
        return self._file.get(ProjectFile.LANGUAGE)

    def get_game(self) -> GameList:
        return GameList(self._file.get(ProjectFile.GAME))

    def get_location(self) -> str:
        return self._file.get(ProjectFile.LOCATION)

    def get_data(self) -> GameFile:
        return GameFile(self._file.get(ProjectFile.DATA))


class GameFile():
    def __init__(self, game: Game):
        self._file = { }

    def to_json(self):
        return self._file

    def to_game(self, game: GameList):
        res = Game()
        for g in GAME_CLASSES:
            if g.get_game() == game:
                res = g()
        return res
