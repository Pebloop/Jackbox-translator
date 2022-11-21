""" Page class for the layout module.

This class is used to create a page for the application.
"""
from typing import List

import PySimpleGUI as sg

from src.components.component import Component
from src.data.appdata import AppData
from src.events.event import Event
from src.utils.align import Align


class Layout(Component):
    """ Page class.

    This class is used to create a page for the application.
    """

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"

    def __init__(self, appdata: AppData):
        """ Page class constructor."""
        super().__init__(appdata)
        self._layout = [[]]
        self._name = "Layout"
        self.align = Align.CENTER
        self.orientation = Layout.HORIZONTAL
        self.sg_component = [[]]
        print("test")
        self.load()

    def refresh(self, event: Event):
        for component in self._layout:
            for e in component:
                e.refresh(event)

    def load(self):
        self.sg_component = []

        for component in self._layout:
            elements = []
            for e in component:
                elements.append(e.display())
            self.sg_component.append(elements)

        self.__manage_orientation()

    def __manage_orientation(self):
        # if self.align == Align.TOP:
        #    self.sg_component = sg.vtop(self.sg_component, expand_x = True, expand_y = True)
        # elif self.align == Align.CENTER:
        #    self.sg_component = sg.vcenter(self.sg_component, expand_x = True, expand_y = True)
        # elif self.align == Align.BOTTOM:
        #    self.sg_component = sg.vbottom(self.sg_component, expand_x = True, expand_y = True)

        justify = "center"
        if self.orientation == Layout.VERTICAL:
            justify = "center"
        elif self.align == Align.LEFT:
            justify = "left"
        elif self.align == Align.RIGHT:
            justify = "right"

        self.sg_component = self.__create_component(self.sg_component, justify)

    def __create_component(self, elements: List[List[sg.Element]], justify: str):
        return sg.Column(elements, expand_x = True, expand_y = True, element_justification = justify, pad = (0, 0))
