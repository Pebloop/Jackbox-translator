"""Component abstract class.

This class is the base class for all components. It provides the basic methods for all components.
"""
from typing import List

import PySimpleGUI as sg

from src.data.appdata import AppData
from src.events.event import Event


class Component:
    """Component class.

    This class is the base class for all components. It provides the basic methods for all components.
    """

    sg_component = None
    _appdata = None

    def __init__(self, appdata: AppData):
        """Component class constructor

        This method is used to initialize the component.
        """
        self._appdata = appdata
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

    def update(self, data: dict):
        """Update the component.

        This method is used to update the component.
        """
        return self.sg_component

    def assign_style(self, style):
        """Assign the style to the component.

        This method is used to assign the style to the component.
        """
        pass
