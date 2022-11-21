"""

"""
from src.data.appdata import AppData
from src.events.event import Event


class EventPageChanged(Event):
    """ Event page changed."""

    def __init__(self, appdata: AppData, layout: str):
        """ Event page changed constructor."""
        super().__init__(appdata)
        self._layout = layout

    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
                "layout": self._layout
                }

    def execute(self):
        """ Execute the event."""
        self._appdata.set_page(self._layout)
