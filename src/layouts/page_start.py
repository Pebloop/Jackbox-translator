import PySimpleGUI as sg
from src.language import get_text
from src.layouts.components.text import Text
from src.layouts.page import Page


class PageStart(Page):
    def _load_projects_layout(self):
        return Text("NO_PROJECTS")

    def reload(self) -> list:
        """ Reload the page.

        This method is used to reload the page.
        :return: The layout of the page.
        """
        self._layout = [
                Text("CURRENT_PROJECTS"),
                self._load_projects_layout()
            ]
        return super().reload()


