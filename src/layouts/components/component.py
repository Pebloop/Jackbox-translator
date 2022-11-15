"""Component abstract class.

This class is the base class for all components. It provides the basic methods for all components.
"""
from typing import List

import PySimpleGUI as sg

from src.events.event import Event


class Component:
    """Component class.

    This class is the base class for all components. It provides the basic methods for all components.
    """

    sg_component = None

    def __init__(self):
        """Component class constructor

        This method is used to initialize the component.
        """
        self.sg_component = sg.Text("")

    def display(self):
        """Display the component.

        This method is used to display the component.
        """
        return self.sg_component

    def refresh(self, events: List[Event]):
        """Refresh the component.

        This method is used to refresh the component.
        """
        return self.sg_component

    def reload(self):
        """Reload the component.

        This method is used to reload the component.
        """
        return self.sg_component

    def update(self, data: dict):
        """Update the component.

        This method is used to update the component.
        """
        return self.sg_component


