from src.data.games.game import Game
from src.data.games.jackbox.minigame import Minigame


class Jackbox(Game):
    _minigames: list[Minigame] = []

    def __init__(self):
        """Jackbox class constructor

        This method is used to initialize the Jackbox class.
        """
        super().__init__()

    def get_minigames(self) -> list[Minigame]:
        """Get the minigames of the game.

        This method is used to get the minigames of the game.
        :return: The minigames of the game.
        """
        return self._minigames

    def get_minigame_list(self) -> list[str]:
        """Get the minigame list of the game."""
        return [minigame.get_name() for minigame in self._minigames]
