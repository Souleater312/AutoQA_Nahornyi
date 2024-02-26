from lesson_16.factory_example.drivers.base_browser import Brawser


class FirefoxBrowser(Brawser):
    _name = "Firefox"

    def __init__(self):
        super().__init__()
