from src.components.button import Button
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event_page_changed import EventPageChanged
from src.layouts.layout_create_project import LayoutCreateProject
from src.utils.align import Align


class LayoutStart(Layout):
    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Text(appdata, "CURRENT_PROJECTS", style = self._appdata.get_style().title1),
                self._load_projects_layout(),
                Button(appdata, Text(appdata, "NEW_PROJECT"), action = lambda: self._create_new_project()),
                ]
        self.load()

    def _load_projects_layout(self):
        if len(self._appdata.get_save_file().get_projects()) > 0:
            return Text(self._appdata, "PROJECTS")
        else:
            return Text(self._appdata, "NO_PROJECTS")

    def _create_new_project(self):
        self._appdata.push_event(EventPageChanged(self._appdata, LayoutCreateProject(self._appdata)))
