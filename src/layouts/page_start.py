from src.components.button import Button
from src.components.page import Page
from src.components.text import Text
from src.utils.style import Style


class PageStart(Page):
    style = Style()

    def __init__(self):
        super().__init__()
        self._layout = [
                [Button(Text("EN"), action = lambda: print("EN"))],
                [Text("CURRENT_PROJECTS", style = self.style.title1)],
                [self._load_projects_layout()]
                ]
        self.load()

    def _load_projects_layout(self):
        return Text("NO_PROJECTS")
