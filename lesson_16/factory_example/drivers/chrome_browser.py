from lesson_16.factory_example.drivers.base_browser import Brawser

class ChromeBrowser(Brawser):
    _name = "Chrome"

    def __init__(self):
        super().__init__()
