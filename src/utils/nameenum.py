"""NameEnum

This script allows easier python Enum in which the name is also the value.
NameEnum also allow enum documentation.

Please follow the following format :

class Vehicles(NameEnum):
    CAR = "Use on the road"
    BOAT = "Use on water"
    PLANE = "Use in the sky"

The value will be the enum name :
>> print(Vehicles.CAR)
"CAR"


Classes
-------
NameEnum
LowerNameEnum
CapitalNameEnum
"""

from enum import Enum


class NameEnum(Enum):
    """Create an enum which the value is the name of the enum"""

    def __new__(cls, doc: str = None):
        self = object.__new__(cls)
        if doc is not None:
            self.__doc__ = doc
        return self

    def __init__(self, doc: str = None):
        if doc is not None:
            self.__doc__ = doc
        self._value_ = self.name

    def __str__(self):
        return str(self._value_)


class LowerNameEnum(NameEnum):
    """Create an enum which the value is the lowercase name of the enum"""

    def __init__(self, doc: str = None):
        super().__init__(doc)
        self._value_ = self.name.lower()


class CapitalNameEnum(NameEnum):
    """Create an enum which the value is the capitalized name of the enum"""

    def __init__(self, doc: str = None):
        super().__init__(doc)
        self._value_ = self.name.capitalize()