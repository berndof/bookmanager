import signal
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController


if __name__ == "__main__":
    app = QApplication([])

    controller = MainController(app)
    controller.show()

    app.exec_()