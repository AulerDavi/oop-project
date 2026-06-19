# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from gui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    
    window = MainWindow()
    window.setWindowIcon(QIcon('icon.png'))
    window.show()
    
    sys.exit(app.exec())
