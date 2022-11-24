from typing import Optional


class TranslationCell:
    _key: Optional[str] = None
    _value: Optional[str] = None
    _original_value: Optional[str] = None

    def is_changed(self):
        return self._value != self._original_value

    def __init__(self, key: str = None, original_value = None, value: Optional[str] = None):
        """TranslationCell class constructor

        This method is used to initialize the TranslationCell class.
        """
        self._key = key
        self._value = value or original_value
        self._original_value = original_value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def get_key(self):
        return self._key

    def get_original_value(self):
        return self._original_value
