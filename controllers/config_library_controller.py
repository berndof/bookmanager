from views.config_library_page import ConfigLibraryPage, Subpage0_SelectBookFile, Subpage1_EditBookInfo
import fitz

class ConfigLibraryController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.view = ConfigLibraryPage(self)
        self.create_pages()

    def create_pages(self):       
        self.subpage0_select_book_file = Subpage0_SelectBookFile(self)
        self.add_page(self.subpage0_select_book_file) #Page 0

        self.subpage1_edit_book_info = Subpage1_EditBookInfo(self)
        self.add_page(self.subpage1_edit_book_info) #Page 1

    def add_page(self, page):
        self.view.page_stack.addWidget(page)

    def go_to_page(self, index):
        self.view.page_stack.setCurrentIndex(index)
    
    def go_to_select_book_file_page(self):
        self.go_to_page(0)

    def go_to_edit_book_info_page(self):
        self.go_to_page(1)

    def handle_select_file(self, file_path):
        
        import os
        destination_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "books") #/books
        
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        
        document = fitz.open(file_path)

        self.subpage1_edit_book_info.load_book_info(document)
        self.go_to_edit_book_info_page()
