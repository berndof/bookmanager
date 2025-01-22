from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Book Manager")
        self.resize(800, 600)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.main_stack = QStackedWidget()
        self.layout.addWidget(self.main_stack)


