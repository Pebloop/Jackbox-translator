from src.data.games.jackbox.minigame import Minigame


class GeneralTJPP4(Minigame):
    _translation_files = ["./templates/games/jackbox/jackbox4/general.json"]

    def __init__(self):
        """Drawful class constructor

        This method is used to initialize the Drawful class.
        """
        super().__init__("General")
