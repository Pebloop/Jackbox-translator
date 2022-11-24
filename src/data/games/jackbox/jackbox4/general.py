import json

from src.data.games.jackbox.minigame import Minigame


class GeneralTJPP4(Minigame):
    _translation_files = ["./templates/games/jackbox/jackbox4/general.json"]

    def __init__(self):
        """Drawful class constructor

        This method is used to initialize the Drawful class.
        """
        super().__init__("General")

    def load_translation(self, path: str) -> None:
        self._translation.get_cells().clear()
        self.__load_localization(path)

    def __load_localization(self, path: str) -> None:
        localization_path = path + "/games/PartyPack/Localization.json"
        try:
            with open(localization_path, "r", encoding = "utf8") as file:
                json_file: dict = json.load(file)
                json_file = json_file.get('table').get('en')
                for key, value in json_file.items():
                    self._translation.add_cell(key = key, original_value = value)
                file.close()
        except FileNotFoundError:
            print("Could not load localization file: " + localization_path)
