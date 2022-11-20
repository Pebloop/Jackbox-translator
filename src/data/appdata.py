""" app data class.

This class is used to store the app general data.

"""
from typing import List

from src.data.language import LanguageManager
from src.data.save_file import SaveFile
from src.events.event import Event
from src.utils.style import Style


class AppData:
    """ App data class.

    This class is used to store the app general data.
    """

    _page = None
    _events: List[Event] = []
    _save_file = None
    _language_manager = None
    _style = None

    def __init__(self):
        """ App data class constructor

        This method is used to initialize the app data.

        """
        from src.layouts.layout_start import LayoutStart

        self._events = []
        self._save_file = SaveFile()
        self._language_manager = LanguageManager(self._save_file.get_language())
        self._style = Style(self)
        self._page = LayoutStart(self)

    def get_page(self):
        """ Get the page.

        This method is used to get the page.
        :return: The page.
        """
        return self._page

    def set_page(self, page):
        """ Set the page.

        This method is used to set the page.
        :param page: The page.
        """
        self._page = page

    def get_events(self) -> List[Event]:
        """ Get the events.

        This method is used to get the events.
        :return: The events.
        """
        return self._events

    def push_event(self, event: Event):
        """ Push an event.

        This method is used to push an event.
        :param event: The event.
        """
        self._events.append(event)

    def pop_event(self) -> Event:
        """ Pop an event.

        This method is used to pop an event.
        :return: The event.
        """
        return self._events.pop()

    def clear_events(self):
        """ Clear the events.

        This method is used to clear the events.
        """
        self._events = []

    def get_save_file(self) -> SaveFile:
        """ Get the save file.

        This method is used to get the save file.
        :return: The save file.
        """
        return self._save_file

    def get_language_manager(self) -> LanguageManager:
        """ Get the language manager.

        This method is used to get the language manager.
        :return: The language manager.
        """
        return self._language_manager

    def get_style(self) -> Style:
        """ Get the style.

        This method is used to get the style.
        :return: The style.
        """
        return self._style
