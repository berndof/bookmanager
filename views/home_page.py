from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListView

class HomePage(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.btn_go_to_config_library = QPushButton("Config Library")
        self.layout.addWidget(self.btn_go_to_config_library)
        self.btn_go_to_config_library.clicked.connect(self.controller.go_to_config_library_page)

        self.label = QLabel("Welcome to Book Manager!")
        self.layout.addWidget(self.label)

        self.book_list = QListView()
        self.layout.addWidget(self.book_list)

        