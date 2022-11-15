""" Event class

This module contains the Event class, which is the base class for all events.
"""


class Event:
    """ Event class

    This class is the base class for all events.
    """

    def __init__(self):
        """ Event class constructor

        This method is used to initialize the event.
        """
        pass

    def get_type(self) -> str:
        """ Get the type of the event.

        This method is used to get the type of the event.
        :return: The type of the event.
        """
        return self.__class__.__name__

    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {}

    def excute(self):
        """ Execute the event.

        This method is used to execute the event.
        """
        pass
