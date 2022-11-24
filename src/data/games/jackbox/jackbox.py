from src.data.games.game import Game
from src.data.games.jackbox.minigame import Minigame
from src.data.translation.translation_cell import TranslationCell


class Jackbox(Game):
    _minigames: list[Minigame] = []
    MAX_DEFAULT_CELL = 50
    _translation_cells: list = []
    _translation_page: int = 0
    _use_default_layout = True

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
        from src.components.button import Button

        right_layout = LayoutChanger(appdata, cls.get_layout_changer(appdata))

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
            cls._use_default_layout = mini.get_layout(appdata) is None
            layout = mini.get_layout(appdata) or cls.get_mini_default_layout(appdata, mini)
            layouts.append((mini.get_name(), Layout(appdata, layout)))
        return layouts

    @classmethod
    def get_mini_default_layout(cls, appdata, mini: Minigame):
        from src.components.layout import Layout
        from src.components.text import Text
        from src.components.button import Button
        translation_layout = cls.get_default_translation_layout(appdata)
        layout = [[Text(appdata, text = mini.get_name(), style = appdata.get_style().title1)],
                  [Button(appdata = appdata, text = Text(appdata, "PREVIOUS"), action = lambda
                      m = mini: cls.__previous(m)),
                   Text(appdata, text = f"Page {cls._translation_page + 1}"),
                   Button(appdata = appdata,
                          text = Text(appdata, "NEXT"),
                          action = lambda m = mini: cls.__next(m))],
                  [Layout(appdata, translation_layout, scrollable = True, size = (800, 400))]]

        return [[Layout(appdata, layout)]]

    @classmethod
    def __next(cls, mini: Minigame):
        if len(mini.get_translation().get_cells()) < cls.MAX_DEFAULT_CELL * (cls._translation_page + 1):
            cls._translation_page += 1
            cls.__update_default_layout(mini)

    @classmethod
    def __previous(cls, mini: Minigame):
        if cls._translation_page > 0:
            cls._translation_page -= 1
            cls.__update_default_layout(mini)

    @classmethod
    def __update_default_layout(cls, mini: Minigame):
        for i in range(len(cls._translation_cells)):
            if i * (cls._translation_page + 1) >= len(mini.get_translation().get_cells()):
                cls._translation_cells[i].set_visible(False)
            else:
                cls._translation_cells[i].set_visible(True)
                cls._translation_cells[i]._layout[0][0].set_text(
                        mini.get_translation().get_cells()[i * (cls._translation_page + 1)].get_key())
                cls._translation_cells[i]._layout[1][0].set_text(
                        mini.get_translation().get_cells()[i * (cls._translation_page + 1)].get_original_value())
                cls._translation_cells[i]._layout[2][0].set_text(
                        mini.get_translation().get_cells()[i * (cls._translation_page + 1)].get_value())

    @classmethod
    def get_default_translation_layout(cls, appdata):
        layout = []
        cls._translation_cells = []
        for i in range(cls.MAX_DEFAULT_CELL):
            cls._translation_cells.append(cls.get_default_translation_cell(appdata, TranslationCell()))
            layout.append([cls._translation_cells[-1]])
        return layout

    @classmethod
    def get_default_translation_cell(cls, appdata, cell: TranslationCell):
        from src.components.layout import Layout
        from src.components.text import Text
        from src.components.input_text import InputText
        from src.utils.font import Font
        return Layout(appdata,
                      [[Text(appdata, text = cell.get_key() or "", font = Font(is_bold = True))],
                       [Text(appdata, text = cell.get_original_value() or "", style = appdata.get_style().quote)],
                       [InputText(appdata)]])

    @classmethod
    def get_mini_layout_general(cls, appdata):
        return None

    def reset_layout(self, path: str):
        for game in self._minigames:
            if self._use_default_layout:
                game.load_translation(path)
                self._translation_page = 0
                self.__update_default_layout(game)
            else:
                game.reset_layout()
