from src.data.games.game import Game
from src.data.games.jackbox.minigame import Minigame
from src.data.translation.translation_cell import TranslationCell


class Jackbox(Game):
    _minigames: list[Minigame] = []

    def __init__(self):
        """Jackbox class constructor

        This method is used to initialize the Jackbox class.
        """
        super().__init__()

    @classmethod
    def get_minigames(cls) -> list[Minigame]:
        """Get the minigames of the game.

        This method is used to get the minigames of the game.
        :return: The minigames of the game.
        """
        return cls._minigames

    def get_minigame_list(self) -> list[str]:
        """Get the minigame list of the game."""
        return [minigame.get_name() for minigame in self._minigames]

    @classmethod
    def get_layout(cls, appdata):
        from src.components.layout import Layout
        from src.components.text import Text
        from src.components.layout_changer import LayoutChanger

        right_layout = LayoutChanger(appdata, cls.get_layout_changer(appdata))
        from src.components.button import Button
        left_layout = []
        for mini in cls._minigames:
            left_layout.append([Button(appdata = appdata,
                                       text = Text(appdata, text = mini.get_name()),
                                       action = lambda x = mini.get_name(): right_layout.change_layout(x))])

        return Layout(appdata, [[Layout(appdata, left_layout), right_layout]])

    @classmethod
    def get_layout_changer(cls, appdata):
        from src.components.layout import Layout
        layouts = []
        for mini in cls._minigames:
            mini.load_translation()
            layout = mini.get_layout(appdata) or cls.get_mini_default_layout(appdata, mini)
            layouts.append((mini.get_name(), Layout(appdata, layout)))
        return layouts

    @classmethod
    def get_mini_default_layout(cls, appdata, mini: Minigame):
        from src.components.layout import Layout
        from src.components.text import Text
        translation_layout = cls.get_default_translation_layout(appdata, mini)
        layout = [[Text(appdata, text = mini.get_name(), style = appdata.get_style().title1)],
                  [Layout(appdata, translation_layout, scrollable = True, size = (500, 400))]]

        return [[Layout(appdata, layout)]]

    @classmethod
    def get_default_translation_layout(cls, appdata, mini):
        layout = []
        for cell in mini.get_translation().get_cells():
            layout.append([cls.get_default_translation_cell(appdata, cell, mini)])
        return layout

    @classmethod
    def get_default_translation_cell(cls, appdata, cell: TranslationCell, mini: Minigame):
        from src.components.layout import Layout
        from src.components.text import Text
        from src.components.input_text import InputText
        return Layout(appdata, [[Text(appdata, text = cell.get_original_value())],
                                [InputText(appdata,
                                           action = lambda x, c = cell: c.set_value(x), size = (68, None))]])

    @classmethod
    def get_mini_layout_general(cls, appdata):
        return None
