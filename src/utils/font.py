"""Font

This module contains the Font class, which is used to represent fonts in the application.
"""

from typing import Optional

import PySimpleGUI as sg

from src.utils.style import Style


class Font:
    """Font class.

    This class is used to represent fonts in the application.
    """

    font: Optional[str] = None
    size: Optional[int] = None
    is_italic = False
    is_bold = False
    is_underline = False
    is_overstrike = False

    def __init__(self,
                 font: Optional[str] = None,
                 size: Optional[int] = None,
                 is_italic: Optional[bool] = None,
                 is_bold: Optional[bool] = None,
                 is_underline: Optional[bool] = None,
                 is_overstrike: Optional[bool] = None):
        """Font class constructor

        This method is used to initialize the font class.
        :param font: The font.
        """

        self.font = font
        self.size = size
        self.is_italic = is_italic
        self.is_bold = is_bold
        self.is_underline = is_underline
        self.is_overstrike = is_overstrike

    @classmethod
    def get_installed_fonts(self):
        """Get installed fonts.

        This method is used to get the installed fonts.
        :return: The installed fonts.
        """
        fonts = sg.Text.fonts_installed_list()
        clean_fonts = []
        for font in fonts:
            splitted = font.split(" ")
            if len(splitted) > 1:
                splitted.remove(splitted[0])
            if splitted[0][0] == '@':
                splitted[0] = splitted[0][1:]
            clean_fonts.append("".join(splitted))

        return clean_fonts

    @classmethod
    def is_font_installed(self):
        """Is font installed.

        This method is used to check if the font is installed.
        :return: True if the font is installed, False otherwise.
        """
        return self.font in self.get_installed_fonts()

    def get_font(self):
        """Get font.

        This method is used to get the font.
        :return: The font.
        """
        style = ""

        style += "italic " if self.is_italic else ""
        style += "bold " if self.is_bold else ""
        style += "underline " if self.is_underline else ""
        style += "overstrike " if self.is_overstrike else ""

        return self.font, self.size or 0, style

    def reset_font_style(self):
        """Reset font style.

        This method is used to reset the font style.
        """
        self.is_italic = None
        self.is_bold = None
        self.is_underline = None
        self.is_overstrike = None

    def assign_style(self, style):
        """Assign style.

        This method is used to assign the style.
        :param style: The style.
        """

        self.is_italic = Style.style_or_custom(self.is_italic, "is_italic", style)
        self.is_bold = Style.style_or_custom(self.is_bold, "is_bold", style)
        self.is_underline = Style.style_or_custom(self.is_underline, "is_underline", style)
        self.is_overstrike = Style.style_or_custom(self.is_overstrike, "is_overstrike", style)
        self.font = Style.style_or_custom(self.font, "font", style)
        self.size = Style.style_or_custom(self.size, "size", style)
