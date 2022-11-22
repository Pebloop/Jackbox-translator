from src.data.games.gamelist import GameList


class MetaProject:
    name: str = ""
    language: str = ""
    game: GameList = GameList.UNKNOWN

    def __init__(self, name: str = "", language: str = "", game: GameList = GameList.UNKNOWN, save_dict: dict = None):
        if save_dict is not None:
            self.name = save_dict.get("name")
            self.language = save_dict.get("language")
            self.game = GameList(save_dict.get("game"))
        else:
            self.name = name
            self.language = language
            self.game = game

    def to_json(self):
        return {
                "name"    : self.name,
                "language": self.language,
                "game"    : self.game.value
                }
