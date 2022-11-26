from typing import List, Optional

from src.data.translation.translation_cell import TranslationCell


class TranslationCellManager:
    _cells: List[TranslationCell] = []

    def __init__(self, cells: List[TranslationCell] = None):
        """TranslationCellManager class constructor

        This method is used to initialize the TranslationCellManager class.
        """
        if cells is not None:
            self._cells = cells

    def __str__(self):
        cells = ""
        for cell in self._cells:
            cells += f"{str(cell)}, "
        return f"TranslationCellManager(cells={cells})"

    def add_cell(self,
                 cell: TranslationCell = None,
                 key: str = "",
                 original_value: str = "",
                 value: Optional[str] = None):
        if cell is not None:
            self._cells.append(cell)
        else:
            if value is None:
                value = original_value
            self._cells.append(TranslationCell(key, original_value, value))

    def get_cells(self) -> List[TranslationCell]:
        return self._cells

    def get_cell(self, key: str) -> Optional[TranslationCell]:
        for cell in self._cells:
            if cell.get_key() == key:
                return cell
        return None

    def get_changed_cells(self) -> List[TranslationCell]:
        changed_cells = []
        for cell in self._cells:
            if cell.is_changed():
                changed_cells.append(cell)
        return changed_cells

    def get_changed_cells_count(self) -> int:
        return len(self.get_changed_cells())

    def is_changed(self) -> bool:
        return self.get_changed_cells_count() > 0

    def get_original_value(self, key: str) -> str:
        cell = self.get_cell(key)
        if cell is not None:
            return cell.get_original_value()
        return ""

    def get_value(self, key: str) -> str:
        cell = self.get_cell(key)
        if cell is not None:
            return cell.get_value()
        return ""

    def set_value(self, key: str, value: str):
        cell = self.get_cell(key)
        if cell is not None:
            cell.set_value(value)

    def get_keys(self) -> List[str]:
        keys = []
        for cell in self._cells:
            keys.append(cell.get_key())
        return keys

    def update(self, key: str, original_value: str, value: str):
        cell = self.get_cell(key)
        if cell is None:
            self.add_cell(key = key, original_value = value)
        else:
            if cell.get_value() is None:
                cell.set_value(value)
            if cell.get_original_value() is None:
                cell._original_value = value
