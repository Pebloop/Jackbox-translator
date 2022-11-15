""" Page class for the layout module.

This class is used to create a page for the application.
"""
from src.events.event import Event
from src.layouts.components.component import Component


class Page(Component):
    """ Page class.

    This class is used to create a page for the application.
    """

    def __init__(self):
        """ Page class constructor."""
        super().__init__()
        self._layout = []
        self.reload()

    def refresh(self, event: Event):
        for component in self._layout:
            if isinstance(e, list):
                for e in component:
                    e.refresh(event)
            else:
                component.refresh(event)

    def _reload_list(self, list: list):
        new_list = []

        for component in list:
            if isinstance(component, list):
                new_list.append(self._reload_list(component))
            else:
                new_list.append(component.reload())
        return new_list

    def reload(self):
        self.sg_component = []

        for component in self._layout:
            if isinstance(component, list):
                self.sg_component.append(self._reload_list(component))
            else:
                self.sg_component.append(component.display())

    def display(self):
        return self.sg_component

