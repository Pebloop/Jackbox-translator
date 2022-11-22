from src.data.games.gamelist import GameList


class Game:

    def __init__(self):
        pass

    @classmethod
    def get_game(cls) -> GameList:
        return GameList.UNKNOWN

    @classmethod
    def is_game(cls, path: str) -> bool:
        return True

    @classmethod
    def get_name(cls) -> str:
        return "Unknown"
