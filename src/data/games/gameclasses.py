from src.data.games.game import Game
from src.data.games.gamelist import GameList
from src.data.games.jackbox.jackbox1.jackbox1 import Jackbox1
from src.data.games.jackbox.jackbox2.jackbox2 import Jackbox2
from src.data.games.jackbox.jackbox3.jackbox3 import Jackbox3
from src.data.games.jackbox.jackbox4.jackbox4 import Jackbox4
from src.data.games.jackbox.jackbox5.jackbox5 import Jackbox5
from src.data.games.jackbox.jackbox6.jackbox6 import Jackbox6
from src.data.games.jackbox.jackbox7.jackbox7 import Jackbox7
from src.data.games.jackbox.jackbox8.jackbox8 import Jackbox8
from src.data.games.jackbox.jackbox9.jackbox9 import Jackbox9

GAME_CLASSES = [
        Jackbox1,
        Jackbox2,
        Jackbox3,
        Jackbox4,
        Jackbox5,
        Jackbox6,
        Jackbox7,
        Jackbox8,
        Jackbox9
        ]


def get_game_class(game: GameList) -> Game:
    for game_class in GAME_CLASSES:
        if game_class.get_game() == game:
            return game_class
    return None
