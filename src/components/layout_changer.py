from typing import List, Tuple

import PySimpleGUI as sg

from src.components.component import Component
from src.components.layout import Layout


class LayoutChanger(Component):
    _layouts: List[Tuple[str, Layout]] = None

    def __init__(self, appdata, layouts: List[Tuple[str, Layout]]):
        super().__init__(appdata)
        self._layouts = layouts

        self.sg_component = []
        for idx, layout in enumerate(self._layouts):
            visible = True if idx == 0 else False
            self.sg_component.append(sg.Column([[layout[1].display()]], visible = visible, key = layout[0]))
        self.sg_component = sg.Column([self.sg_component], expand_x = True, expand_y = True)

    def refresh(self, event):
        for layout in self._layouts:
            layout[1].refresh(event)

    def change_layout(self, layout: str):
        for idx, layout_ in enumerate(self._layouts):
            if layout_[0] == layout:
                self.sg_component.Rows[0][idx].update(visible = True)
            else:
                self.sg_component.Rows[0][idx].update(visible = False)
        self._appdata.get_window().refresh()

    def display(self):
        return self.sg_component
