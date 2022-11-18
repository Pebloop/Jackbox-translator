""" A button component.

This module contains the Text component for the layout.
"""
from typing import Optional

from src.events.event import Event
from src.utils.color import Color
from src.utils.language import get_text
from src.components.component import Component
import PySimpleGUI as sg


class Text(Component):
    key: str = ""
    text: str = ""

    def __init__(self, key: str, color: Optional[Color] = None):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param key: The key of the text.
        :param color: The color of the text.
        """
        super().__init__()

        hex_color = color.get_hex() if color is not None else ""

        self.key = key
        self.text = get_text(self.key)
        self.sg_component = sg.Text(self.text, text_color=hex_color)

    def _load_text(self):
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        self.text = get_text(self.key)
        self.sg_component.update(self.text)

    def refresh(self, event: Event):
        """ Refresh the text.

        This method is used to refresh the text.
        :param event: The events.
        """
        print(event.get_type())
        if event.get_type() == "EventLanguageChanged":
            self._load_text()

    def reload(self):
        """ Reload the text.

        This method is used to reload the text.
        :return: The text.
        """
        self._load_text()
        return self.sg_component
