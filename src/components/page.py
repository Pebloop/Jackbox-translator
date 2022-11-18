""" Page class for the layout module.

This class is used to create a page for the application.
"""
from src.events.event import Event
from src.components.component import Component


class Page(Component):
    """ Page class.

    This class is used to create a page for the application.
    """

    def __init__(self):
        """ Page class constructor."""
        super().__init__()
        self._layout = []
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
                self.sg_component.append(self._reload_list(component))
            else:
                self.sg_component.append(component.display())

    def display(self):
        return [self.sg_component]

