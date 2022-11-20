""" A text component.

This module contains the Text component for the layout.
"""
from __future__ import annotations

from typing import Optional

import PySimpleGUI as sg

from src.components.component import Component
from src.events.event import Event
from src.utils.color import Color
from src.utils.font import Font
from src.utils.language import get_text
from src.utils.style import Style


class Text(Component):
    key: str = ""
    text: str = ""
    color: Color = None
    background_color: Color = None
    font: Font = None

    def __init__(self,
                 key: str,
                 color: Optional[Color] = None,
                 background_color: Optional[Color] = None,
                 font: Optional[Font] = None,
                 style: Optional[Text] = None):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param key: The key of the text.
        :param color: The color of the text.
        """
        super().__init__()

        self.assign_style(style)

        self.key = key
        self.text = get_text(self.key)
        self.color = color or self.color
        self.background_color = background_color or self.background_color

        if font:
            self.font.size = font.size or self.font.size
            self.font.font = font.font or self.font.font
            self.font.is_bold = font.is_bold or self.font.is_bold
            self.font.is_italic = font.is_italic or self.font.is_italic
            self.font.is_underline = font.is_underline or self.font.is_underline
            self.font.is_overstrike = font.is_overstrike or self.font.is_overstrike

        hex_color = self.color.get_hex() if self.color is not None else ""
        hex_background_color = self.background_color.get_hex() if self.background_color is not None else None
        font = self.font.get_font() if self.font is not None else None

        self.sg_component = sg.Text(self.text,
                                    text_color = hex_color,
                                    background_color = hex_background_color,
                                    font = font,
                                    key = str(id(self)))

    def load_text(self) -> str:
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        return get_text(self.key)

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
        self.sg_component.update(text_color = hex_color)

    def set_background_color(self, background_color: Color):
        """ Set the background color of the text.

        This method is used to set the background color of the text.
        :param background_color: The background color of the text.
        """
        self.background_color = background_color
        hex_background_color = background_color.get_hex() if background_color is not None else None
        self.sg_component.update(background_color = hex_background_color)

    def assign_style(self, style):
        """ Assign the style to the text.

        This method is used to assign the style to the text.
        :param style: The style to assign.
        """
        if self.font is None:
            self.font = Font()

        if style is None:
            return

        self.color = Style.style_or_custom(self.color, 'color', style)
        self.background_color = Style.style_or_custom(self.background_color, 'background_color', style)
        self.font.assign_style(style.font)
