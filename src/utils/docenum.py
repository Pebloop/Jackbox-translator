"""DocEnum

This script allows python Enum to be documented.
Please follow the following format :

class Vehicles(DocEnum):
    CAR = 0, "Use on the road"
    BOAT = 1, "Use on water"
    PLANE = 2, "Use in the sky"
"""

from enum import Enum


class DocEnum(Enum):
    """This class make enum documentation easier

    The only difference with python enum is the possibility to document enum values.
    Usage is as follows :

    class <class name>(DocEnum):
        <name> = <value>, <doc>

    Example :

    class Vehicles(DocEnum):
        CAR = 0, "Use on the road"
        BOAT = 1, "Use on water"
        PLANE = 2, "Use in the sky"
    """
    def __new__(cls, value: object, doc: str = None):
        self = object.__new__(cls)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self