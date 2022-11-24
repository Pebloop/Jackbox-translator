"""

"""
from src.data.appdata import AppData
from src.data.projects.metaproject import MetaProject
from src.events.event import Event
from src.utils.override import Overrides


class EventProjectSelected(Event):
    """ Event project selected."""

    def __init__(self, appdata: AppData, project: MetaProject):
        """ Event page changed constructor."""
        super().__init__(appdata)
        self._project: MetaProject = project

    @Overrides
    def get_data(self) -> dict:
        """ Get the data of the event.

        This method is used to get the data of the event.
        :return: The data of the event.
        """
        return {
                "project": self._project,
                }

    @Overrides
    def execute(self):
        """ Execute the event."""
        self._appdata.get_project_manager().set_project(self._project)
