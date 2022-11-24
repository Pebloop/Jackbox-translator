from typing import List

from src.components.layout import Layout
from src.data.appdata import AppData
from src.data.projects.metaproject import MetaProject
from src.events.event import Event
from src.layouts.project_element import ProjectElement


class ProjectElementManager(Layout):
    MAX_PROJECTS = 100
    _elements: List[Layout] = []

    def __init__(self,
                 appdata: AppData):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self._layout = self.get_elements()
        self._scrollable = True
        self.load()

    def refresh(self, event: Event):
        super().refresh(event)

        if event.get_type() == "EventProjectCreated":
            nb_projects = len(self._appdata.get_save_file().get_projects())

            if nb_projects >= self.MAX_PROJECTS:
                return

            project: MetaProject = event.get_data().get("project")
            new_project_layout = self._elements[nb_projects]
            new_project_layout._layout[0][0].set_game(project)
            new_project_layout.set_visible(True)
            x, y = self.sg_component.get_size()
            self.sg_component.set_size((x, y + 10))
            self._appdata.get_window().refresh()

    def get_elements(self) -> list:
        projects_layout = []

        for project in self._appdata.get_save_file().get_projects():
            self._elements.append(Layout(self._appdata, [[ProjectElement(self._appdata, project)]]))
            projects_layout.append([self._elements[-1]])

        for i in range(len(projects_layout), self.MAX_PROJECTS):
            self._elements.append(Layout(self._appdata, [[ProjectElement(self._appdata)]], visible = False))
            projects_layout.append([self._elements[-1]])

        return projects_layout
