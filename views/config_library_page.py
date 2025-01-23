from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListView, QStackedWidget, QFileDialog, QMessageBox

class ConfigLibraryPage(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Configurações da Biblioteca")
        self.layout.addWidget(self.label)

        self.page_stack = QStackedWidget()
        self.layout.addWidget(self.page_stack)

class Subpage0_SelectBookFile(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Selecione o arquivo de configuração")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Selecionar")
        self.button.clicked.connect(self.show_select_file_dialog)

        self.layout.addWidget(self.button)

    def show_select_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Add New Book", "", "PDF Files (*.pdf)", options=options)

        if file_path.endswith('.pdf') or file_path.endswith('.epub'):
            self.controller.handle_select_file(file_path)
        else:
            QMessageBox.warning(None, "Formato inválido", "Por favor, escolha um arquivo no formato PDF ou EPUB.")

class Subpage1_EditBookInfo(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Editando livro")
        self.layout.addWidget(self.label)

    def load_book_info(self, document):
        self.document = document
        self.label.setText(f"Editando livro: {document.metadata}")