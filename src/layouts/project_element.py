from src.components.button import Button
from src.components.image import Image
from src.components.layout import Layout
from src.components.text import Text
from src.data.appdata import AppData


class ProjectElement(Layout):
    def __init__(self,
                 appdata: AppData,
                 title: str,
                 image: str,
                 description: str):
        """ Input text class constructor

            This method is used to initialize the input text component.
            :param appdata: The application data.
        """
        print("ProjectElement")
        super().__init__(appdata)
        self._title = title
        self._image = image
        self._layout = [[Image(appdata, image, size = (64, 64)),
                         Layout(appdata,
                                [[Text(appdata, text = title)],
                                 [Text(appdata, text = description)]]),
                         Button(appdata, Text(appdata, "OPEN"), action = lambda: print("test"))
                         ]]
        self.load()
