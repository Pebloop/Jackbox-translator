from enum import Enum


class MinigameStatus(Enum):
    """Minigame status enum."""
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"


class Minigame:
    _name = ""
    _status = MinigameStatus.NOT_STARTED

    def __init__(self, name: str):
        """Minigame class constructor

        This method is used to initialize the Minigame class.
        """
        self._name = name

    def get_name(self):
        return self._name
