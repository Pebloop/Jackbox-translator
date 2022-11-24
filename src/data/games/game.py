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

    @classmethod
    def get_image(cls) -> str:
        return "./res/unknown.png"

    @classmethod
    def get_layout(cls, appdata):
        from src.components.layout import Layout
        from src.components.text import Text
        return Layout(appdata, [[Text(appdata, text = "No game layout found.")]])

    def reset_layout(self, path: str):
        pass
