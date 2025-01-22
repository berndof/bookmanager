from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListView

class ConfigLibraryPage(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Config_library_page")
        self.layout.addWidget(self.label)

        