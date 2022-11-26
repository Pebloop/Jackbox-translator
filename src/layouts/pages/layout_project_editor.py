from typing import Optional

import PySimpleGUI as sg

from src.components.button import Button
from src.components.file_browser import FileBrowser
from src.components.file_saver import FileSaver
from src.components.input_text import InputText
from src.components.layout import Layout
from src.components.layout_changer import LayoutChanger
from src.components.text import Text
from src.data.appdata import AppData
from src.data.games.gameclasses import GAME_CLASSES, get_game_class
from src.data.projects.project import Project
from src.events.event import Event
from src.events.event_page_changed import EventPageChanged
from src.utils.align import Align
from src.utils.override import Overrides


class LayoutProjectEditor(Layout):
    _project: Optional[Project] = None

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT

        self._language = Text(appdata, text = "[.]")
        self._title = Text(appdata, text = ".", style = self._appdata.get_style().title1)
        self._game_layout = LayoutChanger(appdata, self._loadGamesLayouts())
        self._export_field = InputText(appdata, visible = False, action = self._export)
        self._export_browser = FileSaver(appdata, Text(appdata, "EXPORT"), (("Translator Box Project", "*.tbp"),))
        self._import_field = InputText(appdata, visible = False, action = self._import)
        self._import_browser = FileBrowser(appdata, Text(appdata, "IMPORT"), (("Translator Box Project", "*.tbp"),))
        self._build_field = InputText(appdata, visible = False, action = self._build)
        self._build_browser = FileSaver(appdata, Text(appdata, "BUILD"), (("ZIP", "*.zip"),))

        self._layout = [
                [Button(appdata, Text(appdata, "BACK"), action = lambda: self._back()),
                 self._export_field, self._export_browser,
                 self._import_field, self._import_browser,
                 self._build_field, self._build_browser],
                [self._language, self._title],
                [self._game_layout]
                ]
        self._project: Optional[Project] = None
        self.load()

    @Overrides
    def refresh(self, event: Event):
        super().refresh(event)

        if event.get_type() == "EventProjectSelected" or event.get_type() == "EventProjectCreated":
            self._project = self._appdata.get_project_manager().get_project()
            self._title.set_text(self._project.get_name())
            self._language.set_text(self._project.get_language())
            self._game_layout.change_layout(get_game_class(self._project.get_game()).get_name())
            self._project.get_data().reset_layout(self._project.get_path())

    def _back(self):
        self._appdata.push_event(EventPageChanged(self._appdata, "start"))
        self._project.save()

    def _export(self, path: str):
        if self._project is not None:
            if self._project.export(path):
                sg.popup("Project exported successfully!")
            else:
                sg.popup("Project export failed!")

    def _import(self, path: str):
        if self._project is not None:
            if self._project.import_(path):
                sg.popup("Project imported successfully!")
            else:
                sg.popup("Project import failed!")

    def _build(self, path: str):
        if self._project is not None:
            self._project.build(path)
            sg.popup("Project built successfully!")

    def _loadGamesLayouts(self):
        layouts = []
        for game in GAME_CLASSES:
            layouts.append((game.get_name(), game.get_layout(self._appdata)))
        return layouts
