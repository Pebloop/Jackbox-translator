from src.data.jackgame import JackGame
from src.data.minigame import Minigame


class Game:
    _minigames: list[Minigame] = []
    _game: JackGame = JackGame.UNKNOWN

    def __init__(self, game: JackGame):
        self._game = game
        self._minigames = []
