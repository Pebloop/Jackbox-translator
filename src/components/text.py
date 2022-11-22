""" A text component.

This module contains the Text component for the layout.
"""
from __future__ import annotations

from typing import Optional

import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData
from src.events.event import Event
from src.utils.align import Align
from src.utils.color import Color
from src.utils.font import Font
from src.utils.override import Overrides
from src.utils.style import Style


class Text(Component):
    key: str = ""
    text: str = ""
    color: Color = None
    background_color: Color = None
    font: Font = None

    def __init__(self,
                 appdata: AppData,
                 key: str = None,
                 text: str = None,
                 color: Optional[Color] = None,
                 background_color: Optional[Color] = None,
                 font: Optional[Font] = None,
                 style: Optional[Text] = None,
                 align: Align = Align.LEFT):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param appdata: The application data.
        :param key: The key of the text.
        :param color: The color of the text.
        :param background_color: The background color of the text.
        :param font: The font of the text.
        :param style: The style of the text.
        """
        super().__init__(appdata)

        self.assign_style(style)

        self.key = key
        self.is_key = key is not None
        self.text = text or self.load_text()
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

        self.sg_component = sg.Column([[sg.Text(self.text,
                                                text_color = hex_color,
                                                background_color = hex_background_color,
                                                font = font,
                                                key = str(id(self)))]], justification = str(align), pad = (0, 0))

    @Overrides
    def refresh(self, event: Event):
        """ Refresh the text.

        This method is used to refresh the text.
        :param event: The events.
        """
        if event.get_type() == "EventLanguageChanged":
            self._load_text()

    def load_text(self) -> str:
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        return self._appdata.get_language_manager().get_text(self.key) if self.is_key else self.text

    def _load_text(self):
        """ Load the text.

        This method is used to load the text.
        :return: The text.
        """
        self.text = self._appdata.get_language_manager().get_text(self.key)
        self.sg_component.Rows[0][0].update(self.text)

    def set_text(self, text: str):
        """ Set the text.

        This method is used to set the text.
        :param text: The text.
        """
        self.text = text
        self.is_key = False
        self.sg_component.Rows[0][0].update(text)

    def get_text(self) -> str:
        """ Get the text.

        This method is used to get the text.
        :return: The text.
        """
        return self.text

    def set_key(self, key: str):
        """ Set the key of the text.

        This method is used to set the key of the text.
        :param key: The key of the text.
        """
        self.key = key
        self.is_key = key is not None
        self._load_text()

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
