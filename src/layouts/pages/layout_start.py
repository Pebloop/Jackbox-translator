from src.components.button import Button
from src.components.custom.project_element import ProjectElement
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event_page_changed import EventPageChanged
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
            return self._load_projects()
        else:
            return Text(self._appdata, "NO_PROJECTS")

    def _load_projects(self):
        projects_layout = []
        for project in self._appdata.get_save_file().get_projects():
            projects_layout.append(ProjectElement(self._appdata, project, "res/tjpp2.png", "test"))

        return projects_layout

    def _create_new_project(self):
        self._appdata.push_event(EventPageChanged(self._appdata, "create_project"))
