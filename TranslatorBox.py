#!/usr/bin/env python3

__version__ = '0.0.0'

from src.language import load_languages

""" TranslatorBox

Translator box is a tool for Jack box Party translations

It has been made by the French Jackbox translation community.
You can find us on discord : https://discord.gg/XhwPfUrCEx

This project is under the Apache 2 license.
"""

import sys
from src.start import launch_window


def main():
    launch_window()


if __name__ == '__main__':
    main()
