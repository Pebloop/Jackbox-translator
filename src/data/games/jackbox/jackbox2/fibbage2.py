from src.data.games.jackbox.minigame import Minigame
from src.data.translation.translation_cell import TranslationCell
from src.data.translation.translation_cell_manager import TranslationCellManager


class Fibbage2(Minigame):
    __translation_tab = [TranslationCell("TEST", "test")]

    _translation = TranslationCellManager(__translation_tab)

    def __init__(self):
        """Fibbage2 class constructor

        This method is used to initialize the Fibbage2 class.
        """
        super().__init__("Fibbage 2")
