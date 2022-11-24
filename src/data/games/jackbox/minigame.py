from enum import Enum

from src.data.translation.translation_cell_manager import TranslationCellManager


class MinigameStatus(Enum):
    """Minigame status enum."""
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"


class Minigame:
    _name = ""
    _status = MinigameStatus.NOT_STARTED
    _translation_files = []
    _translation: TranslationCellManager = TranslationCellManager()

    def __init__(self, name: str):
        """Minigame class constructor

        This method is used to initialize the Minigame class.
        """
        self._name = name

    def get_name(self):
        return self._name

    def get_translation(self) -> TranslationCellManager:
        return self._translation

    def get_status(self) -> MinigameStatus:
        return self._status

    def set_status(self, status: MinigameStatus):
        self._status = status

    def is_finished(self) -> bool:
        return self._status == MinigameStatus.FINISHED

    def is_in_progress(self) -> bool:
        return self._status == MinigameStatus.IN_PROGRESS

    def is_not_started(self) -> bool:
        return self._status == MinigameStatus.NOT_STARTED

    @classmethod
    def get_layout(self, appdata):
        return None

    def load_translation(self, path: str):
        pass

    def reset_layout(self):
        self.load_translation()
        pass
