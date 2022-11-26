from typing import List, Tuple

from src.data.games.gamelist import GameList
from src.data.translation.translation_cell_manager import TranslationCellManager

TranslationManager = List[Tuple[str, TranslationCellManager]]


class Game:
    _translation: TranslationManager = []

    def __init__(self):
        pass

    @classmethod
    def get_game(cls) -> GameList:
        return GameList.UNKNOWN

    @classmethod
    def is_game(cls, path: str) -> bool:
        return True

    @classmethod
    def get_name(cls) -> str:
        return "Unknown"

    @classmethod
    def get_image(cls) -> str:
        return "./res/unknown.png"

    @classmethod
    def get_layout(cls, appdata):
        from src.components.layout import Layout
        from src.components.text import Text
        return Layout(appdata, [[Text(appdata, text = "No game layout found.")]])

    def reset_layout(self, path: str):
        pass

    def get_translation(self) -> TranslationManager:
        return self._translation

    def set_translations(self):
        pass
