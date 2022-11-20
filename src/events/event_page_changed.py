"""

"""
from src.components.layout import Layout
from src.data.appdata import AppData
from src.events.event import Event


class EventPageChanged(Event):
    """ Event page changed."""

    def __init__(self, appdata: AppData, layout: Layout):
        """ Event page changed constructor."""
        super().__init__(appdata)
        self.layout = layout

    def execute(self):
        """ Execute the event."""
        self._appdata.set_page(self.layout)
