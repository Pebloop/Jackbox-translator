import PySimpleGUI as sg

from src.components.component import Component
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event import Event


class FileSaver(Component):
    def __init__(self,
                 appdata: AppData, text: Text, file_types: any):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        super().__init__(appdata)
        self._text_obj = text
        self._file_types = file_types
        self._text = self._text_obj.load_text()
        self.sg_component = sg.FileSaveAs(button_text = self._text,
                                          enable_events = True,
                                          file_types = file_types)

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
        self._text_obj.refresh(event)
