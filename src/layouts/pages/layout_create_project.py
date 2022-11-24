from typing import Optional

import PySimpleGUI as sg

from src.components.browser import Browser
from src.components.button import Button
from src.components.input_text import InputText
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.data.games.game import Game
from src.data.games.gameclasses import GAME_CLASSES
from src.data.projects.metaproject import MetaProject
from src.data.projects.project import GameList, Project
from src.events.event_page_changed import EventPageChanged
from src.events.event_project_created import EventProjectCreated
from src.utils.align import Align


class LayoutCreateProject(Layout):

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                [Button(appdata, Text(appdata, "BACK"), action = lambda: self._back()),
                 Text(appdata, "NEW_PROJECT", style = self._appdata.get_style().title1)],
                [Text(appdata, "PROJECT_NAME"), InputText(appdata)],
                [Text(appdata, "PROJECT_LANGUAGE"), InputText(appdata)],
                [Text(appdata, "GAME_LOCATION"), InputText(appdata, action = self._check_game), Browser(appdata)],
                [Text(appdata, "PROJECT_GAME"), Text(appdata, "GAME_UNKNOWN")],
                [Button(appdata, Text(appdata, "CREATE"), action = lambda: self._create_new_project())]
                ]
        self._project_name = self._layout[1][1]
        self._project_language = self._layout[2][1]
        self._project_location = self._layout[3][1]
        self._layout_game = self._layout[4][1]
        self._game = GameList.UNKNOWN
        self._game_class: Optional[Game] = None
        self.load()

    def _check_game(self, x: str):
        for game_class in GAME_CLASSES:
            if game_class.is_game(self._project_location.get_text()):
                self._game = game_class.get_game()
                self._game_class = game_class
                self._layout_game.set_text(game_class.get_name())
                return
        self._game = GameList.UNKNOWN
        self._layout_game.set_key("GAME_UNKNOWN")

    def _back(self):
        self._appdata.push_event(EventPageChanged(self._appdata, "start"))

    def _create_new_project(self):
        if self._project_name.get_text() == "":
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_INVALID_NAME"))
            return
        for idx in range(len(self._appdata.get_project_manager().get_projects())):
            if self._appdata.get_project_manager().get_projects()[idx].name == self._project_name.get_text():
                sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_EXISTS"))
                return
        if self._project_language.get_text() == "":
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_INVALID_LANGUAGE"))
            return

        if self._game is not GameList.UNKNOWN:
            self._appdata.get_project_manager().create_project(Project(self._project_name.get_text(),
                                                                       self._project_language.get_text(),
                                                                       self._project_location.get_text(),
                                                                       self._game))
            meta = MetaProject(self._project_name.get_text(), self._project_language.get_text(), self._game,
                               self._game_class.get_image())
            self._appdata.push_event(EventProjectCreated(self._appdata, meta))
            self._appdata.push_event(EventPageChanged(self._appdata, "project_editor"))
        else:
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_UNKNOWN_GAME"))
