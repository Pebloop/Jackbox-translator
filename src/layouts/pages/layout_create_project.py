import os

import PySimpleGUI as sg

from src.components.browser import Browser
from src.components.button import Button
from src.components.input_text import InputText
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.data.project import Game, Project
from src.events.event_page_changed import EventPageChanged
from src.events.event_project_created import EventProjectCreated
from src.utils.align import Align


class LayoutCreateProject(Layout):

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Button(appdata, Text(appdata, "BACK"), action = lambda: self._back()),
                Text(appdata, "NEW_PROJECT", style = self._appdata.get_style().title1),
                [Text(appdata, "PROJECT_NAME"), InputText(appdata)],
                [Text(appdata, "PROJECT_LANGUAGE"), InputText(appdata)],
                [Text(appdata, "GAME_LOCATION"), InputText(appdata, action = self._check_game), Browser(appdata)],
                [Text(appdata, "PROJECT_GAME"), Text(appdata, "GAME_UNKNOWN")],
                Button(appdata, Text(appdata, "CREATE"), action = lambda: self._create_new_project())
                ]
        self._project_name = self._layout[2][1]
        self._project_language = self._layout[3][1]
        self._project_location = self._layout[4][1]
        self._project_game = self._layout[5][1]
        self._layout_game = self._layout[5][1]
        self._game = Game.UNKNOWN
        self.load()

    def _check_game(self):
        game: Game = Game.UNKNOWN
        if os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack.exe"):
            game = Game.JACKBOX1
            self._layout_game.set_text("The Jackbox Party Pack")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 2.exe"):
            game = Game.JACKBOX2
            self._layout_game.set_text("The Jackbox Party Pack 2")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 3.exe"):
            game = Game.JACKBOX3
            self._layout_game.set_text("The Jackbox Party Pack 3")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 4.exe"):
            game = Game.JACKBOX4
            self._layout_game.set_text("The Jackbox Party Pack 4")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 5.exe"):
            game = Game.JACKBOX5
            self._layout_game.set_text("The Jackbox Party Pack 5")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 6.exe"):
            game = Game.JACKBOX6
            self._layout_game.set_text("The Jackbox Party Pack 6")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 7.exe"):
            game = Game.JACKBOX7
            self._layout_game.set_text("The Jackbox Party Pack 7")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 8.exe"):
            game = Game.JACKBOX8
            self._layout_game.set_text("The Jackbox Party Pack 8")
        elif os.path.exists(self._project_location.get_text() + "/The Jackbox Party Pack 9.exe"):
            game = Game.JACKBOX9
            self._layout_game.set_text("The Jackbox Party Pack 9")
        else:
            game = Game.UNKNOWN
            self._layout_game.set_key("GAME_UNKNOWN")
        self._game = game

    def _back(self):
        self._appdata.push_event(EventPageChanged(self._appdata, "start"))

    def _create_new_project(self):
        if self._project_name.get_text() == "":
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_INVALID_NAME"))
            return
        for idx in range(len(self._appdata.get_project_manager().get_projects())):
            if self._appdata.get_project_manager().get_projects()[idx] == self._project_name.get_text():
                sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_EXISTS"))
                return
        if self._project_language.get_text() == "":
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_PROJECT_INVALID_LANGUAGE"))
            return

        if (self._game is not Game.UNKNOWN):
            self._appdata.get_project_manager().create_project(Project(self._project_name.get_text(),
                                                                       self._project_language.get_text(),
                                                                       self._project_location.get_text(),
                                                                       Game.JACKBOX2))
            self._appdata.push_event(EventProjectCreated(self._appdata, self._project_name.get_text()))
            self._appdata.push_event(EventPageChanged(self._appdata, "project_main"))
        else:
            sg.Popup(self._appdata.get_language_manager().get_text("ERROR_CREATE_UNKNOWN_GAME"))
