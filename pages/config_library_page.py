from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Signal


class ConfigLibraryPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.create_pages()

    def init_ui(self):
        self.layout = QVBoxLayout()

        label = QLabel("Configurações da Biblioteca")
        self.layout.addWidget(label)

        self.page_stack = QStackedWidget()
        self.layout.addWidget(self.page_stack)

        self.btn_go_back = QPushButton("Voltar")
        self.layout.addWidget(self.btn_go_back)
        self.btn_go_back.clicked.connect(self.parent.go_to_initial_page)

        self.setLayout(self.layout)

    def create_pages(self):

        self.subpage0_select_file = Subpage0_SelectFile(self)
        self.subpage1_edit_file_info = Subpage1_EditFileInfo(self)

        self.page_stack.addWidget(self.subpage0_select_file) # subpágina 0
        self.page_stack.addWidget(self.subpage1_edit_file_info) # subpágina 1


class Subpage0_SelectFile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        label = QLabel("Adicionar Novo Livro - Passo 1")
        self.layout.addWidget(label)

        # Select File Button
        self.btn_select_file = QPushButton("Selecionar arquivo")
        self.btn_select_file.clicked.connect(self.handle_btn_select_file)
        self.layout.addWidget(self.btn_select_file)

        self.setLayout(self.layout)

    def handle_btn_select_file(self):  
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Add New Book", "", "PDF Files (*.pdf)", options=options)

        if file_path.endswith('.pdf') or file_path.endswith('.epub'):

            self.parent.subpage1_edit_file_info.load_file(file_path)
            self.parent.page_stack.setCurrentIndex(1)

        else:
            QMessageBox.warning(None, "Formato inválido", "Por favor, escolha um arquivo no formato PDF ou EPUB.")

class Subpage1_EditFileInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

        self.file_path:str

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_filename = QLabel("Adicionar Novo Livro - Passo 2")
        self.layout.addWidget(self.label_filename)

        self.setLayout(self.layout)

    def load_file(self, file_path:str):
        self.set_file_path(file_path)

        self.label_filename.setText(f"Arquivo selecionado: {file_path}")
        print(f"File name set to: {file_path}")

    def set_file_path(self, file_path:str):
        self.file_path = file_path