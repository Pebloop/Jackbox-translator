from src.components.button import Button
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event_language_changed import EventLanguageChanged
from src.utils.align import Align


class LayoutStart(Layout):

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Button(appdata, Text(appdata, "LANG"), action = lambda: self._switch_language()),
                Text(appdata, "CURRENT_PROJECTS", style = self._appdata.get_style().title1),
                self._load_projects_layout(),
                Button(appdata, Text(appdata, "NEW_PROJECT"), action = lambda: appdata.get_save_file().save()),
                ]
        self.load()

    def _load_projects_layout(self):
        if len(self._appdata.get_save_file().get_projects()) > 0:
            return Text(self._appdata, "PROJECTS")
        else:
            return Text(self._appdata, "NO_PROJECTS")

    def _switch_language(self):
        """ Switch the language.

        This method is used to switch the language.
        :param appdata: The application data.
        """
        print("Switching language...")
        print("Current language: " + self._appdata.get_language_manager().get_current_language())

        if self._appdata.get_language_manager().get_current_language() == "EN":
            self._appdata.push_event(EventLanguageChanged(self._appdata, "FR"))
        else:
            self._appdata.push_event(EventLanguageChanged(self._appdata, "EN"))
