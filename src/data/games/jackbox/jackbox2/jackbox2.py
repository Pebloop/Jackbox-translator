import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.data.games.jackbox.jackbox2.bidiots import Bidiots
from src.data.games.jackbox.jackbox2.bombcorp import BombCorp
from src.data.games.jackbox.jackbox2.earwax import Earwax
from src.data.games.jackbox.jackbox2.fibbage2 import Fibbage2
from src.data.games.jackbox.jackbox2.quiplashxl import QuiplashXL
from src.utils.override import Overrides


class Jackbox2(Jackbox):
    _name = "The Jackbox Party Pack 2"

    def __init__(self):
        """Jackbox2 class constructor

        This method is used to initialize the Jackbox2 class.
        """
        super().__init__()
        self._minigames = [
                Fibbage2(),
                Earwax(),
                Bidiots(),
                QuiplashXL(),
                BombCorp()
                ]

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX2

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack 2.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack 2"
