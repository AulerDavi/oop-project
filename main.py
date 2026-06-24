# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from gui import MainWindow
from utils import resource_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('icon.ico')))
    
    window = MainWindow()
    window.setWindowIcon(QIcon(resource_path('icon.ico')))
    window.show()
    
    sys.exit(app.exec())
