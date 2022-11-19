""" Event class

This module contains the Event class, which is the base class for all events.
"""
from src.events.event import Event


class EventSimplePyGui(Event):
    event = None
    values = { }

    """ Event class

    This class is the base class for all events.
    """

    def __init__(self, event = None, values = { }):
        """ Event class constructor

        This method is used to initialize the event.
        """
        self.event = event

    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
                "event": self.event,
                }

    def execute(self):
        """ Execute the event.

        This method is used to execute the event.
        """
        pass
