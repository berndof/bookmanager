import sys
from PySide6.QtWidgets import QApplication
from ui import MainWindow
from api import API


if __name__ == "__main__":
    Qapp = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(Qapp.exec())

