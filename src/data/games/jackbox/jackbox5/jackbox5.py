import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.utils.override import Overrides


class Jackbox5(Jackbox):
    _name = "The Jackbox Party Pack 5"

    def __init__(self):
        """Jackbox5 class constructor

        This method is used to initialize the Jackbox5 class.
        """
        super().__init__()
        self._minigames = [
                ]

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX2

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack 5.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack 5"

    @classmethod
    @Overrides
    def get_image(cls) -> str:
        return "./res/tjpp5.png"
