from src.data.games.gameclasses import GAME_CLASSES
from src.data.games.gamelist import GameList


class MetaProject:
    name: str = ""
    language: str = ""
    game: GameList = GameList.UNKNOWN
    image: str = ""

    def __init__(self,
                 name: str = "",
                 language: str = "",
                 game: GameList = GameList.UNKNOWN,
                 image: str = "",
                 save_dict:
                 dict = None):
        if save_dict is not None:
            self.name = save_dict.get("name")
            self.language = save_dict.get("language")
            self.game = GameList(save_dict.get("game"))
            self.image = save_dict.get("image")
        else:
            self.name = name
            self.language = language
            self.game = game
            self.image = image

    def to_json(self):
        return {
                "name"    : self.name,
                "language": self.language,
                "game"    : self.game.value,
                "image"   : self.image
                }

    def get_game_name(self):
        name = "unknown"
        for game in GAME_CLASSES:
            if game.get_game() == self.game:
                name = game.get_name()
                break
        return name
