import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.data.games.jackbox.jackbox1.drawful import Drawful
from src.data.games.jackbox.jackbox1.fibbagexl import FibbageXL
from src.data.games.jackbox.jackbox1.lieswatter import LieSwatter
from src.data.games.jackbox.jackbox1.wordspud import WordSpud
from src.data.games.jackbox.jackbox1.youdontknowjack2015 import YouDontKnowJack2015
from src.utils.override import Overrides


class Jackbox1(Jackbox):
    _name = "The Jackbox Party Pack 2"

    def __init__(self):
        """Jackbox2 class constructor

        This method is used to initialize the Jackbox2 class.
        """
        super().__init__()
        self._minigames = [
                YouDontKnowJack2015(),
                FibbageXL(),
                Drawful(),
                WordSpud(),
                LieSwatter()
                ]

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX1

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack"
