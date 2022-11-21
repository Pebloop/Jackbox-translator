from src.components.layout import Layout
from src.data.appdata import AppData


class ProjectElementManager(Layout):
    def __init__(self,
                 appdata: AppData,
                 elements: list):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        print("ProjectElement")
        super().__init__(appdata)
        self.orientation = Layout.VERTICAL
        self._layout = [elements]
        self.load()
