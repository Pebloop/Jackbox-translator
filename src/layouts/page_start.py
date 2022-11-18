from src.components.text import Text
from src.components.page import Page
from src.utils.font import Font


class PageStart(Page):

    def __init__(self):
        super().__init__()
        self._layout = [
            [Text("CURRENT_PROJECTS", font=Font(is_bold=True, size=24, is_underline=True))],
            [self._load_projects_layout()]
        ]
        self.load()


    def _load_projects_layout(self):
        return Text("NO_PROJECTS")


