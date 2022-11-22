import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.utils.override import Overrides


class Jackbox4(Jackbox):
    _name = "The Jackbox Party Pack 2"

    def __init__(self):
        """Jackbox4 class constructor

        This method is used to initialize the Jackbox4 class.
        """
        super().__init__()
        self._minigames = [
                ]

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX4

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack 4.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack 4"