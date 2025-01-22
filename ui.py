from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QListView
import pages


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.create_pages()

    def init_ui(self):
        self.setWindowTitle("Book Manager")
        self.resize(800, 600)

        self.main_stack = QStackedWidget()

        self.setCentralWidget(self.main_stack)
    
    def create_pages(self):
        # Criar as páginas
        self.initial_page = pages.InitialPage(self)
        self.config_library_page = pages.ConfigLibraryPage(self)

        # Adicionar as páginas ao StackedWidget
        self.main_stack.addWidget(self.initial_page)          # Página 0
        self.main_stack.addWidget(self.config_library_page)   # Página 1

    def go_to_config_library_page(self):
        #TODO abstraction - mapping pages to indexes, clean this piece of code
        self.main_stack.setCurrentIndex(1)

    def go_to_initial_page(self):
        self.main_stack.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
