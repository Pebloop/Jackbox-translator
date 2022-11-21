""" Page class for the layout module.

This class is used to create a page for the application.
"""

from src.components.layout import Layout
from src.data.appdata import AppData


class Frame(Layout):
    """ Page class.

    This class is used to create a page for the application.
    """

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"

    def __init__(self, appdata: AppData):
        """ Page class constructor."""
        super().__init__(appdata)
        self._title = ""
        self.load()

