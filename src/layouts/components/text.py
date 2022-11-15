""" A text component.

This module contains the Text component for the layout.
"""
from typing import List

from src.events.event import Event
from src.language import get_current_language, get_text
from src.layouts.components.component import Component
import PySimpleGUI as sg

class Text(Component):
    key: str = ""
    text: str = ""

    def __init__(self, key: str):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param key: The key of the text.
        """
        self.key = key
        self.sg_component = sg.Text("")
        self.reload()

    def _load_text(self):
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        self.text = get_text(self.key)
        self.sg_component = [sg.Text(self.text)]

    def refresh(self, event: Event):
        """ Refresh the text.

        This method is used to refresh the text.
        :param event: The events.
        """
        print(event.get_type())
        if event.get_type() == "LANGUAGE_CHANGED":
            self._load_text()

    def reload(self):
        """ Reload the text.

        This method is used to reload the text.
        :return: The text.
        """
        self._load_text()
        print(self.sg_component)
        return self.sg_component

