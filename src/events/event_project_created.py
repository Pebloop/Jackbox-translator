"""

"""
from src.data.appdata import AppData
from src.events.event import Event


class EventProjectCreated(Event):
    """ Event page changed."""

    def __init__(self, appdata: AppData, name: str):
        """ Event page changed constructor."""
        super().__init__(appdata)
        self._name = name

    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
                "name": self._name
                }

    def execute(self):
        """ Execute the event."""
