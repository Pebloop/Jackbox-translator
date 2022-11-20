from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData
from src.utils.align import Align


class LayoutCreateProject(Layout):
    def __init__(self, appdata: AppData):
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self.align = Align.LEFT
        self._layout = [
                Text(appdata, "NEW_PROJECT", style = self._appdata.get_style().title1),
                ]
        self.load()

    def _create_new_project(self):
        pass
