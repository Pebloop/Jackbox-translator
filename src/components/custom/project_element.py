import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData


class ProjectElement(Component):
    def __init__(self,
                 appdata: AppData,
                 title: str,
                 image: str,
                 description: str):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)
        self._title = title
        self._image = image

        self.sg_component = sg.Frame(layout = [[sg.Image(image), sg.Text(description)]], title = title)
