"""Style

This module contains the Style class, which is used to define the style of the app.
"""
from src.utils.utils import safe_member


class Style:
    """Style class.

    This class is used to define the style of the app.
    """

    def __init__(self, appdata):
        """Style class constructor

        This method is used to initialize the style class.
        """
        from src.components.text import Text
        from src.utils.font import Font

        self.appdata = appdata
        self.theme = ""

        self.title1 = Text(appdata, "title1", font = Font(size = 18, is_bold = True, is_underline = True))
        self.title2 = Text(appdata, "title2", font = Font(size = 16, is_bold = True))
        self.title3 = Text(appdata, "title3")
        self.title4 = Text(appdata, "title4")
        self.title5 = Text(appdata, "title5")

        self.text = Text(appdata, "text")
        self.quote = Text(appdata, "quote", font = Font(size = 10, is_italic = True))
        self.link = Text(appdata, "link")

    @classmethod
    def style_or_custom(cls, value, value_name: str, style):
        return value or safe_member(style, value_name)
