from src.components.button import Button
from src.components.layout import Layout
from src.components.layout_changer import LayoutChanger
from src.components.text import Text
from src.data.appdata import AppData
from src.events.event_language_changed import EventLanguageChanged
from src.layouts.layout_create_project import LayoutCreateProject
from src.layouts.layout_start import LayoutStart
from src.utils.align import Align


class LayoutMain(Layout):
    _page = None,

    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Button(appdata, Text(appdata, "LANG"), action = lambda: self._switch_language()),
                LayoutChanger(appdata, [
                        ("start", LayoutStart(appdata)),
                        ("create_project", LayoutCreateProject(appdata))
                        ])
                ]
        self._page = self._layout[1]
        self.load()

    def change_page(self, page: Layout):
        self._page.change_layout("create_project")
        self._page.update({ })

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
