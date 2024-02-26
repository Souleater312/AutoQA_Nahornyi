from lesson_17.factories.abc_beer_factory import BeerFactory
from lesson_17.factories.sorts_of_bear.ale import Ale
from lesson_17.factories.sorts_of_bear.lager import Lager


class LagerFactory(BeerFactory):
    _beer_type = "lager"

    def __init__(self):
        self.name = "Rogan"
        self._positions = ["lager", "ale"]

    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == "lager":
            return Lager()
        elif name == "ale":
            return Ale()