"""

"""
from src.data.appdata import AppData
from src.data.games.gamelist import GameList
from src.events.event import Event
from src.utils.override import Overrides


class EventProjectCreated(Event):
    """ Event page changed."""

    def __init__(self, appdata: AppData, name: str, language: str, game: GameList):
        """ Event page changed constructor."""
        super().__init__(appdata)
        self._name = name
        self._language = language
        self._game = game

    @Overrides
    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
                "name"    : self._name,
                "language": self._language,
                "game"    : self._game
                }

    @Overrides
    def execute(self):
        """ Execute the event."""
