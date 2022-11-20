""" app data class.

This class is used to store the app general data.

"""
from typing import List

from PySimpleGUI import Window

from src.data.manager.language_manager import LanguageManager
from src.data.manager.project_manager import ProjectManager
from src.data.save_file import SaveFile
from src.events.event import Event
from src.utils.style import Style


class AppData:
    """ App data class.

    This class is used to store the app general data.
    """

    _main_page = None
    _page = None
    _events: List[Event] = []
    _save_file = None
    _language_manager = None
    _style = None
    _project_manager = None
    _window: Window = None

    def __init__(self):
        """ App data class constructor

        This method is used to initialize the app data.

        """
        from src.layouts.layout_main import LayoutMain
        from src.layouts.layout_start import LayoutStart

        self._window = None
        self._events = []
        self._save_file = SaveFile()
        self._language_manager = LanguageManager(self._save_file.get_language())
        self._project_manager = ProjectManager(self._save_file.get_projects())
        self._style = Style(self)
        self._page = LayoutStart(self)
        self._main_page = LayoutMain(self)

    def set_window(self, window: Window):
        """ Set the window.

        This method is used to set the window.
        :param window: The window.
        """
        self._window = window

    def get_window(self) -> Window:
        """ Get the window.

        This method is used to get the window.
        :return: The window.
        """
        return self._window

    def get_main_page(self):
        """ Get the main page.

        This method is used to get the main page.
        :return: The main page.
        """
        return self._main_page

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
        self._main_page.change_page(page)

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
