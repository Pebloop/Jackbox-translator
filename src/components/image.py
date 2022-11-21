import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData


class Image(Component):
    def __init__(self,
                 appdata: AppData,
                 path: str,
                 size: tuple = None):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)

        self._path = path
        self.sg_component = sg.Image(path, size = size)
