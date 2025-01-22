from views.main_window import MainWindow
from controllers.home_controller import HomeController
from controllers.config_library_controller import ConfigLibraryController

class MainController:
    def __init__(self, app):
        self.app = app
        self.view = MainWindow(self)

        self.home_controller = HomeController(self)
        self.config_library_controller = ConfigLibraryController(self)

        self.add_page(self.home_controller.view) # Page 0
        self.add_page(self.config_library_controller.view) # Page 1
        
    def show(self):
        self.view.show()
        self.app.exec()
    
    def go_to_initial_page(self):
        self.go_to_page(0)
    
    def go_to_config_library_page(self):
        self.go_to_page(1)

    def add_page(self, page):
        self.view.main_stack.addWidget(page)

    def go_to_page(self, index):
        self.view.main_stack.setCurrentIndex(index)