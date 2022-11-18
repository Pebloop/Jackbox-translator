""" Event : Language changed

This module contains the EventLanguageChanged class, which is used to notify the application that the language has changed.
"""

from src.events.event import Event
from src.utils.language import load_language, get_current_language


class EventLanguageChanged(Event):
    """ Event : Language changed

    This class is used to notify the application that the language has changed.
    """

    def __init__(self, new_language: str):
        """ Event : Language changed

        This method is used to initialize the event.
        """
        super().__init__()
        self._original_language = get_current_language()
        self._new_language = new_language

    def get_original_language(self) -> str:
        """ Get the original language.

        This method is used to get the original language.
        :return: The original language.
        """
        return self._original_language

    def get_new_language(self) -> str:
        """ Get the new language.

        This method is used to get the new language.
        :return: The new language.
        """
        return self._new_language

    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
            "original_language": self._original_language,
            "new_language": self._new_language
        }

    def execute(self):
        load_language(self._new_language)
