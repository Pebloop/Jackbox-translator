""" A text component.

This module contains the Text component for the layout.
"""
from __future__ import annotations

from types import FunctionType
from typing import Optional

import PySimpleGUI as sg

from src.components.component import Component
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event import Event
from src.utils.font import Font
from src.utils.style import Style


class Button(Component):
    text: Text = None
    action: FunctionType = None

    def __init__(self,
                 appdata: AppData,
                 text: Optional[Text] = None,
                 action: () = None):
        """ Text class constructor.

        This method is used to initialize the text component.
        :param text: The text.
        :param action: The action to execute when the button is clicked.
        """
        super().__init__(appdata)

        # self.assign_style(style)

        self.text = text
        self.action = action

        color_hex = self.text.color.get_hex() if self.text.color is not None else None
        background_color_hex = self.text.background_color.get_hex() if self.text.background_color is not None else None

        self.sg_component = sg.Button(button_text = self.text.text,
                                      font = self.text.font.get_font(),
                                      button_color = (color_hex, background_color_hex),
                                      enable_events = True,
                                      key = str(id(self)))

    def refresh(self, event: Event):
        """ Refresh the text.

        This method is used to refresh the text.
        :param event: The events.
        """
        if event.get_type() == "EventSimplePyGui":
            if event.get_data().get("event") == str(id(self)):
                self.action() if self.action is not None else None
        if event.get_type() == "EventLanguageChanged":
            self.sg_component.update(text = self.text.load_text())

    def reload(self):
        """ Reload the text.

        This method is used to reload the text.
        :return: The text.
        """
        self.sg_component.update(text = self.text.load_text())
        return self.sg_component

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
