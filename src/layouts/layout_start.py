from src.appdata import AppData
from src.components.button import Button
from src.components.layout import Layout
from src.components.text import Text
from src.events.event_language_changed import EventLanguageChanged
from src.utils.align import Align
from src.utils.language import get_current_language
from src.utils.style import Style


def switch_language(appdata: AppData):
    """ Switch the language.

    This method is used to switch the language.
    :param appdata: The application data.
    """
    print("Switching language...")
    print("Current language: " + get_current_language())

    if get_current_language() == "EN":
        appdata.push_event(EventLanguageChanged("FR"))
    else:
        appdata.push_event(EventLanguageChanged("EN"))


class LayoutStart(Layout):
    style = Style()

    def __init__(self, appdata: AppData):
        super().__init__()
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Button(Text("LANG"), action = lambda: switch_language(appdata)),
                Text("CURRENT_PROJECTS", style = self.style.title1),
                self._load_projects_layout()
                ]
        self.load()

    def _load_projects_layout(self):
        return Text("NO_PROJECTS")
