from views.config_library_page import ConfigLibraryPage

class ConfigLibraryController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        #self.model = 
        self.view = ConfigLibraryPage(self)

