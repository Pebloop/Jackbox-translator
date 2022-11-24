import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.data.games.jackbox.jackbox4.general import GeneralTJPP4
from src.utils.override import Overrides


class Jackbox4(Jackbox):
    _name = "The Jackbox Party Pack 2"
    _minigames = [
            GeneralTJPP4(),
            ]

    def __init__(self):
        """Jackbox4 class constructor

        This method is used to initialize the Jackbox4 class.
        """
        super().__init__()

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

    @classmethod
    @Overrides
    def get_image(cls) -> str:
        return "./res/tjpp4.png"
