import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData
from src.events.event import Event


class InputText(Component):
    def __init__(self,
                 appdata: AppData,
                 action: () = None,
                 size: tuple = (None, None)):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)

        self.action = action
        self.sg_component = sg.InputText(enable_events = True, key = str(id(self)), expand_x = True, size = size)

    def refresh(self, event: Event):
        """ Refresh the text.

            This method is used to refresh the text.
            :param event: The events.
        """
        if event.get_type() == "EventSimplePyGui":
            if event.get_data().get("event") == str(id(self)):
                self.action(self.get_text()) if self.action is not None else None

    def get_text(self) -> str:
        """ Get the text.

            This method is used to get the text.
            :return: The text.
        """
        return self.sg_component.get()

    def set_text(self, text: str):
        """ Set the text.

            This method is used to set the text.
            :param text: The text.
        """
        self.sg_component.update(value = text)
