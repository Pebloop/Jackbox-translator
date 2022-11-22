from src.components.layout import Layout
from src.data.appdata import AppData
from src.events.event import Event
from src.layouts.project_element import ProjectElement


class ProjectElementManager(Layout):
    def __init__(self,
                 appdata: AppData):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        print("ProjectElement")
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self._layout = self.get_elements()
        self.load()

    def refresh(self, event: Event):
        print(self.sg_component.Rows)

        if event.get_type() == "EventProjectCreated":
            print("testzred")

    def get_elements(self) -> list:
        projects_layout = []

        for project in self._appdata.get_save_file().get_projects():
            projects_layout.append([ProjectElement(self._appdata, project, "res/tjpp2.png", "test")])

        return projects_layout
