from abc import ABC


class Brawser(ABC):
    _name = ""

    def __init__(self):
        self.history = []