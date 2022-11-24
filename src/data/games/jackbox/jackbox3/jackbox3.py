import os

from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox import Jackbox
from src.data.games.jackbox.jackbox3.fakinit import FakinIt
from src.data.games.jackbox.jackbox3.general import GeneralTJPP3
from src.data.games.jackbox.jackbox3.guesspionage import Guesspionage
from src.data.games.jackbox.jackbox3.quiplash2 import Quiplash2
from src.data.games.jackbox.jackbox3.teeko import TeeKO
from src.data.games.jackbox.jackbox3.triviamurderparty import TriviaMurderParty
from src.utils.override import Overrides


class Jackbox3(Jackbox):
    _name = "The Jackbox Party Pack 2"
    _minigames = [
            GeneralTJPP3(),
            Quiplash2(),
            TriviaMurderParty(),
            Guesspionage(),
            TeeKO(),
            FakinIt()
            ]

    def __init__(self):
        """Jackbox2 class constructor

        This method is used to initialize the Jackbox2 class.
        """
        super().__init__()

    @classmethod
    @Overrides
    def get_game(cls) -> GameList:
        return GameList.JACKBOX3

    @classmethod
    @Overrides
    def is_game(cls, path: str) -> bool:
        if os.path.exists(path + "/The Jackbox Party Pack 3.exe"):
            return True
        return False

    @classmethod
    @Overrides
    def get_name(cls) -> str:
        return "The Jackbox Party Pack 3"

    @classmethod
    @Overrides
    def get_image(cls) -> str:
        return "./res/tjpp3.png"
