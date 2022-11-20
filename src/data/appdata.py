""" app data class.

This class is used to store the app general data.

"""
from typing import List

from src.data.save_file import SaveFile
from src.events.event import Event


class AppData:
    """ App data class.

    This class is used to store the app general data.
    """

    _page = None
    _events: List[Event] = []
    _save_file = None

    def __init__(self):
        """ App data class constructor

        This method is used to initialize the app data.

        """
        from src.layouts.layout_start import LayoutStart

        self._events = []
        self._save_file = SaveFile()
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
