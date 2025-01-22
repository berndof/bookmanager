from views.home_page import HomePage

class HomeController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        #self.model = 
        self.view = HomePage(self)
        