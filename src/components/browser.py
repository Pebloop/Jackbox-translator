import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData
from src.events.event import Event


class Browser(Component):
    def __init__(self,
                 appdata: AppData):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)
        self._text = self.load_text()

        self.sg_component = sg.FolderBrowse(button_text = self._text, enable_events = True)

    def load_text(self) -> str:
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        return self._appdata.get_language_manager().get_text("BROWSE")

    def _load_text(self):
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        self.text = self._appdata.get_language_manager().get_text("BROWSE")
        self.sg_component.update(text = self.text)

    def refresh(self, event: Event):
        """ Refresh the text.

        This method is used to refresh the text.
        :param event: The events.
        """
        if event.get_type() == "EventLanguageChanged":
            self._load_text()
