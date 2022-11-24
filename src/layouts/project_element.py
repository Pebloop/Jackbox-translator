from typing import List, Optional

from src.components.button import Button
from src.components.component import Component
from src.components.image import Image
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.data.projects.metaproject import MetaProject
from src.events.event_page_changed import EventPageChanged
from src.events.event_project_selected import EventProjectSelected


class ProjectElement(Layout):
    def __init__(self,
                 appdata: AppData,
                 project: Optional[MetaProject] = None):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
            :param project: The project to display.
        """
        super().__init__(appdata)
        self._project = project

        image = project.image if project is not None else "res/unknown.png"
        name = project.name if project is not None else "Unknown"
        language = project.language if project is not None else "XX"
        game_name = project.get_game_name() if project is not None else "Unknown"

        self._layout: List[List[Component]] = [[Image(appdata, image, size = (128, 128)),
                                                Layout(appdata,
                                                       [[Text(appdata, text = "[" + language + "]"),
                                                         Text(appdata, text = name)],
                                                        [Text(appdata, text = game_name)]]),
                                                Button(appdata, Text(appdata, "OPEN"), action = self._action_button)
                                                ]]
        self._layout_image: Image = self._layout[0][0]
        self._layout_name: Text = self._layout[0][1]._layout[0][1]
        self._layout_language: Text = self._layout[0][1]._layout[0][0]
        self._layout_game_name: Text = self._layout[0][1]._layout[1][0]
        self.load()

    def _action_button(self):
        self._appdata.push_event(EventProjectSelected(self._appdata, self._project))
        self._appdata.push_event(EventPageChanged(self._appdata, "project_editor"))

    def set_game(self, game: Optional[MetaProject] = None):
        self._project = game
        self._layout_image.set_image(game.image if game is not None else "res/unknown.png")
        self._layout_name.set_text(game.name if game is not None else "Unknown")
        self._layout_language.set_text("[" + game.language + "]" if game is not None else "XX")
        self._layout_game_name.set_text(game.get_game_name() if game is not None else "Unknown")
        self._appdata.get_window().refresh()
