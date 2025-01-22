from views.main_window import MainWindow
from controllers.home_controller import HomeController

class MainController:
    def __init__(self, app):
        self.app = app
        self.view = MainWindow(self)

        self.home_controller = HomeController(self)
        self.view.add_page(self.home_controller.view)
        

    def show(self):
        self.view.show()
        self.app.exec()
    
