# utils.py
import os
import sys

def resource_path(relative_path: str) -> str:
    try:
        # PyInstaller cria um atributo _MEIPASS no módulo sys
        base_path = sys._MEIPASS
    except AttributeError:
        # Em ambiente de desenvolvimento normal
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
