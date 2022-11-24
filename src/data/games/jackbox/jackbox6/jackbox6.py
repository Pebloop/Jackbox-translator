import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.utils.override import Overrides


class Jackbox6(Jackbox):
    _name = "The Jackbox Party Pack 6"

    def __init__(self):
        """Jackbox6 class constructor

        This method is used to initialize the Jackbox6 class.
        """
        super().__init__()
        self._minigames = [
                ]

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX6

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack 6.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack 6"

    @classmethod
    @Overrides
    def get_image(cls) -> str:
        return "./res/tjpp6.png"