from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QPushButton

class InitialPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Bem-vindo à interface inicial!")
        self.layout.addWidget(self.label)

        #List widget for book - temporary
        self.book_list = QListView()
        self.layout.addWidget(self.book_list)

        self.btn_go_to_config_library = QPushButton("Ir para Configurações da Biblioteca")
        self.btn_go_to_config_library.clicked.connect(self.main_window.go_to_config_library_page)

        self.layout.addWidget(self.btn_go_to_config_library)

        self.setLayout(self.layout)
