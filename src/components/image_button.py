import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData
from src.events.event import Event


class ImageButton(Component):
    def __init__(self,
                 appdata: AppData,
                 path: str,
                 action: () = None):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)

        self._path = path
        self.action = action
        self.sg_component = sg.Image(enable_events = True, key = str(id(self)), source = path)

    def refresh(self, event: Event):
        """ Refresh the text.

            This method is used to refresh the text.
            :param event: The events.
        """
        if event.get_type() == "EventSimplePyGui":
            if event.get_data().get("event") == str(id(self)):
                self.action() if self.action is not None else None
