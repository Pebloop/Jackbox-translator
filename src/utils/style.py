"""Style

This module contains the Style class, which is used to define the style of the app.
"""
from src.utils.utils import safe_member


class Style:
    """Style class.

    This class is used to define the style of the app.
    """

    def __init__(self):
        """Style class constructor

        This method is used to initialize the style class.
        """
        from src.components.text import Text
        from src.utils.font import Font

        self.theme = ""

        self.title1 = Text("title1", font = Font(size = 18, is_bold = True, is_underline = True))
        self.title2 = Text("title2")
        self.title3 = Text("title3")
        self.title4 = Text("title4")
        self.title5 = Text("title5")

        self.text = Text("text")
        self.quote = Text("quote")
        self.link = Text("link")

    @classmethod
    def style_or_custom(cls, value, value_name: str, style):
        return value or safe_member(style, value_name)
