from typing import Optional

from src.components.button import Button
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

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                [Button(appdata, Text(appdata, "BACK"), action = lambda: self._back()),
                 Button(appdata, Text(appdata, "EXPORT"), action = lambda: self._export()),
                 Button(appdata, Text(appdata, "IMPORT"), action = lambda: self._import()),
                 Button(appdata, Text(appdata, "BUILD"), action = lambda: self._build())],
                [Text(appdata, text = "[.]"),
                 Text(appdata, text = ".", style = self._appdata.get_style().title1)],
                [LayoutChanger(appdata,
                               self._loadGamesLayouts())]
                ]
        self._language: Text = self._layout[1][0]
        self._title: Text = self._layout[1][1]
        self._game_layout: LayoutChanger = self._layout[2][0]
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

    def _export(self):
        pass

    def _import(self):
        pass

    def _build(self):
        pass

    def _loadGamesLayouts(self):
        layouts = []
        for game in GAME_CLASSES:
            layouts.append((game.get_name(), game.get_layout(self._appdata)))
        return layouts
