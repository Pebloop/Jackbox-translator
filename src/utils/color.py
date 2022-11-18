"""Color

This module contains the Color class, which is used to represent colors in the application.
"""


class Color:
    """ Color

    This class is used to represent colors in the application.
    """

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    DARK_RED = (139, 0, 0)
    DARK_GREEN = (0, 100, 0)
    DARK_BLUE = (0, 0, 139)
    DARK_YELLOW = (139, 139, 0)
    DARK_CYAN = (0, 139, 139)
    DARK_MAGENTA = (139, 0, 139)
    DARK_WHITE = (192, 192, 192)
    GREY = (128, 128, 128)
    DARK_GREY = (169, 169, 169)
    LIGHT_GREY = (211, 211, 211)
    LIGHT_BLUE = (173, 216, 230)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_RED = (255, 182, 193)
    LIGHT_YELLOW = (255, 255, 224)
    LIGHT_CYAN = (224, 255, 255)
    LIGHT_MAGENTA = (255, 224, 255)

    def __init__(self, rgb: tuple[int, int, int]):
        """ Color class constructor

            This method is used to initialize the color.
            :param rgb: The RGB value.
        """
        self._red = rgb[0]
        self._green = rgb[1]
        self._blue = rgb[2]

    def get_red(self) -> int:
        """ Get the red value.

        This method is used to get the red value.
        :return: The red value.
        """
        return self._red

    def get_green(self) -> int:
        """ Get the green value.

        This method is used to get the green value.
        :return: The green value.
        """
        return self._green

    def get_blue(self) -> int:
        """ Get the blue value.

        This method is used to get the blue value.
        :return: The blue value.
        """
        return self._blue

    def get_rgb(self) -> tuple:
        """ Get the RGB value.

        This method is used to get the RGB value.
        :return: The RGB value.
        """
        return self._red, self._green, self._blue

    def get_hex(self) -> str:
        """ Get the hexadecimal value.

        This method is used to get the hexadecimal value.
        :return: The hexadecimal value.
        """
        return "#%02x%02x%02x" % (self._red, self._green, self._blue)

    def get_rgb_string(self) -> str:
        """ Get the RGB string.

        This method is used to get the RGB string.
        :return: The RGB string.
        """
        return f"rgb({self._red}, {self._green}, {self._blue})"
