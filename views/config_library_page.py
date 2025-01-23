from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListView, QStackedWidget, QFileDialog, QMessageBox, QLineEdit
from PySide6.QtGui import QPixmap


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

        self.label_file = QLabel("Nenhum arquivo selecionado")
        self.layout.addWidget(self.label_file)

        self.init_book_fields()

        self.button_select_file = QPushButton("Selecionar")
        self.button_select_file.clicked.connect(self.show_select_file_dialog)
        self.layout.addWidget(self.button_select_file)

        self.button_save = QPushButton("Salvar")
        self.button_save.setVisible(False)
        #self.button_save.clicked.connect(self.save_book)
        self.layout.addWidget(self.button_save)

    def init_book_fields(self):

        self.cover_label = QLabel()
        self.layout.addWidget(self.cover_label)
        self.cover_label.setVisible(False)
        
        self.title_label = QLabel("Título")
        self.title_label.setVisible(False)
        self.layout.addWidget(self.title_label)
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Título")
        self.title_edit.setVisible(False)
        self.layout.addWidget(self.title_edit)

        self.author_label = QLabel("Autor")
        self.author_label.setVisible(False)
        self.layout.addWidget(self.author_label)
        self.author_edit = QLineEdit()
        self.author_edit.setPlaceholderText("Autor")
        self.author_edit.setVisible(False)
        self.layout.addWidget(self.author_edit)

        self.subject_label = QLabel("Assunto")
        self.subject_label.setVisible(False)
        self.layout.addWidget(self.subject_label)
        self.subject_edit = QLineEdit()
        self.subject_edit.setPlaceholderText("Assunto")
        self.subject_edit.setVisible(False)
        self.layout.addWidget(self.subject_edit)

        self.keywords_label = QLabel("Palavras-chave")
        self.keywords_label.setVisible(False)
        self.layout.addWidget(self.keywords_label)
        self.keywords_edit = QLineEdit()
        self.keywords_edit.setPlaceholderText("Palavras-chave")
        self.keywords_edit.setVisible(False)
        self.layout.addWidget(self.keywords_edit)

    def show_select_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Add New Book", "", "PDF Files (*.pdf)", options=options)

        if file_path.endswith('.pdf') or file_path.endswith('.epub'):
            self.selected_file_path = file_path
            self.controller.load_book()
        else:
            QMessageBox.warning(None, "Formato inválido", "Por favor, escolha um arquivo no formato PDF ou EPUB.")

    def update_book_info(self, book_info):
        self.title_edit.setText(book_info.get('title', ''))
        self.author_edit.setText(book_info.get('author', ''))
        self.subject_edit.setText(book_info.get('subject', ''))
        self.keywords_edit.setText(book_info.get('keywords', ''))
        self.label_file.setText(self.selected_file_path)

    def show_book_info(self):
        self.update_book_info(self.controller.selected_document.metadata)

        cover_pixmap = QPixmap(self.controller.cover_image_path)
        self.cover_label.setPixmap(cover_pixmap)
        self.cover_label.setVisible(True)
        
        self.title_label.setVisible(True)
        self.title_edit.setVisible(True)
        
        self.author_label.setVisible(True)
        self.author_edit.setVisible(True)
        
        self.subject_label.setVisible(True)
        self.subject_edit.setVisible(True)

        self.keywords_label.setVisible(True)
        self.keywords_edit.setVisible(True)

        self.button_select_file.setText("Selecionar outro arquivo")
        self.button_save.setVisible(True)

        
        
        
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
        """ Update ui with document metadata """
    
        self.document = document
        
        self.label.setText(f"Editando livro: {document.metadata}")
