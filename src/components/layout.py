""" Page class for the layout module.

This class is used to create a page for the application.
"""

import PySimpleGUI as sg

from src.components.component import Component
from src.events.event import Event
from src.utils.align import Align


class Layout(Component):
    """ Page class.

    This class is used to create a page for the application.
    """

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"

    def __init__(self):
        """ Page class constructor."""
        super().__init__()
        self._layout = []
        self.align = Align.CENTER
        self.orientation = Layout.HORIZONTAL
        self.load()

    def refresh_list(self, list_: list):
        for component in list_:
            if isinstance(component, list):
                self.refresh_list(component)
            else:
                component.refresh()

    def refresh(self, event: Event):
        for component in self._layout:
            if isinstance(component, list):
                for e in component:
                    e.refresh(event)
            else:
                component.refresh(event)

    def _load_list(self, list_: list):
        new_list = []

        for component in list_:
            if isinstance(component, list):
                new_list.append(self._load_list(component))
            else:
                new_list.append(component.display())
        return new_list

    def load(self):
        self.sg_component = []

        for component in self._layout:
            if isinstance(component, list):
                self.sg_component.append(self._load_list(component))
            else:
                self.sg_component.append(component.display())

        if self.align == Align.TOP:
            self.sg_component = sg.vtop(self.sg_component, expand_x = True, expand_y = True)
        elif self.align == Align.CENTER:
            self.sg_component = sg.vcenter(self.sg_component, expand_x = True, expand_y = True)
        elif self.align == Align.BOTTOM:
            self.sg_component = sg.vbottom(self.sg_component, expand_x = True, expand_y = True)

        if self.orientation == Layout.VERTICAL:
            justify = "center"
            if self.align == Align.LEFT:
                justify = "left"
            elif self.align == Align.RIGHT:
                justify = "right"
            elements = []
            for element in self.sg_component:
                elements.append([element])
            self.sg_component = sg.Column(elements, expand_x = True, expand_y = True, element_justification = justify)

        self.sg_component = [self.sg_component]

    def _reload_list(self, list_: list):
        new_list = []

        for component in list_:
            if isinstance(component, list):
                new_list.append(self._reload_list(component))
            else:
                new_list.append(component.reload())
        return new_list

    def reload(self):
        self.sg_component = []

        for component in self._layout:
            if isinstance(component, list):
                if self.orientation == Layout.VERTICAL:
                    self.sg_component.append([self._reload_list(component)])
                else:
                    self.sg_component.append(self._reload_list(component))
            else:
                if self.orientation == Layout.VERTICAL:
                    self.sg_component.append([component.reload()])
                else:
                    self.sg_component.append(component.reload())

    def display(self):
        return [self.sg_component]
