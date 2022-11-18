""" A text component.

This module contains the Text component for the layout.
"""
from typing import Optional

from src.events.event import Event
from src.utils.color import Color
from src.utils.font import Font
from src.utils.language import get_text
from src.components.component import Component
import PySimpleGUI as sg


class Text(Component):
    key: str = ""

    text: str = ""
    color: Color = None
    background_color: Color = None

    def __init__(self, key: str, color: Optional[Color] = None, background_color: Optional[Color] = None, font: Optional[Font] = None):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param key: The key of the text.
        :param color: The color of the text.
        """
        super().__init__()

        hex_color = color.get_hex() if color is not None else ""
        hex_background_color = background_color.get_hex() if background_color is not None else None
        font = font.get_font() if font is not None else None

        self.key = key
        self.text = get_text(self.key)
        self.color = color
        self.background_color = background_color
        self.font = font
        self.sg_component = sg.Text(self.text, text_color=hex_color, background_color=hex_background_color, font=font)

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

    def set_color(self, color: Color):
        """ Set the color of the text.

        This method is used to set the color of the text.
        :param color: The color of the text.
        """
        self.color = color
        hex_color = color.get_hex() if color is not None else ""
        self.sg_component.update(text_color=hex_color)

    def set_background_color(self, background_color: Color):
        """ Set the background color of the text.

        This method is used to set the background color of the text.
        :param background_color: The background color of the text.
        """
        self.background_color = background_color
        hex_background_color = background_color.get_hex() if background_color is not None else None
        self.sg_component.update(background_color=hex_background_color)

